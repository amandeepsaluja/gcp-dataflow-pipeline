import argparse
import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions


# Define a custom DoFn to extract the specified fields from nested JSON
class ExtractFields(beam.DoFn):
    def __init__(self, fields_to_extract):
        self.fields_to_extract = fields_to_extract

    def process(self, element):
        import json

        try:
            # creating a list of fields to extract from string
            fields_to_extract = self.fields_to_extract.split(",")

            extracted_data = {}
            for field in fields_to_extract:
                # Split the field name by '.' to navigate nested structures
                field_parts = field.split(".")
                current_data = element
                for part in field_parts:
                    if part in current_data:
                        current_data = current_data[part]
                    else:
                        # Field not found, skip this field
                        current_data = None
                        break

                if current_data is not None:
                    extracted_data[field] = current_data

            if extracted_data:
                yield extracted_data
        except (json.JSONDecodeError, ValueError) as e:
            # Handle JSON decoding errors here
            pass


class AddDatetimeAndDate(beam.DoFn):
    def process(self, element):
        from datetime import datetime

        new_element = dict(element)  # Create a copy of the original dictionary

        current_time = datetime.now()

        # Add a DATETIME column with the current timestamp
        new_element["load_datetime"] = current_time
        new_element["load_date"] = current_time.date()

        yield new_element  # Emit the new dictionary with the added columns


def run():
    import requests

    parser = argparse.ArgumentParser()

    # # Set the required arguments
    parser.add_argument(
        "--apiEndpoint", help="API Endpoint for the data", required=True
    )
    parser.add_argument(
        "--fieldsToExtract",
        help="Fields to extract from the JSON response",
        required=True,
    )
    parser.add_argument(
        "--tempLocation", help="GCS Temp location for Dataflow", required=True
    )
    parser.add_argument("--dataset", help="BigQuery Dataset", required=True)
    parser.add_argument("--table", help="BigQuery Table", required=True)
    # parser.add_argument("--schema", help="BigQuery Schema", required=True)

    args, beam_args = parser.parse_known_args()
    beam_options = PipelineOptions(beam_args)

    with beam.Pipeline(options=beam_options) as p:
        json_data = (
            p
            | "Read API" >> beam.Create([args.apiEndpoint])
            | "HTTP GET" >> beam.ParDo(lambda url: requests.get(url).json())
            | "Extract Fields" >> beam.ParDo(ExtractFields(args.fieldsToExtract))
            | "AddDatetimeAndDate" >> beam.ParDo(AddDatetimeAndDate())
            | "Write to BigQuery"
            >> beam.io.WriteToBigQuery(
                table=args.table,
                dataset=args.dataset,
                # schema=args.schema,
                schema="SCHEMA_AUTODETECT",
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                custom_gcs_temp_location=args.tempLocation,
            )
        )

    # Run the pipeline
    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
