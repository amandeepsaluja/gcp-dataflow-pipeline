import argparse
import apache_beam as beam

from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions


class CustomPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        # # Set the required arguments
        parser.add_value_provider_argument(
            "--apiEndpoint", help="API Endpoint for the data", required=True
        )
        parser.add_value_provider_argument(
            "--fieldsToExtract",
            help="Fields to extract from the JSON response",
            required=True,
        )
        parser.add_value_provider_argument(
            "--custom_gcs_temp_location",
            help="GCS Temp location for Dataflow",
            required=True,
        )
        parser.add_value_provider_argument(
            "--dataset", help="BigQuery Dataset", required=True
        )
        parser.add_value_provider_argument(
            "--table", help="BigQuery Table", required=True
        )


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


def run(argv=None):
    import requests

    parser = argparse.ArgumentParser()

    known_args, pipeline_args = parser.parse_known_args(argv)

    global cloud_options
    global custom_options

    pipeline_options = PipelineOptions(pipeline_args)
    cloud_options = pipeline_options.view_as(GoogleCloudOptions)
    custom_options = pipeline_options.view_as(CustomPipelineOptions)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        json_data = (
            p
            | "Read API" >> beam.Create([custom_options.apiEndpoint.get()])
            | "HTTP GET" >> beam.ParDo(lambda url: requests.get(url).json())
            | "Extract Fields"
            >> beam.ParDo(ExtractFields(custom_options.fieldsToExtract.get()))
            | "AddDatetimeAndDate" >> beam.ParDo(AddDatetimeAndDate())
            | "Write to BigQuery"
            >> beam.io.WriteToBigQuery(
                table=custom_options.table.get(),
                dataset=custom_options.dataset.get(),
                schema="SCHEMA_AUTODETECT",
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                custom_gcs_temp_location=custom_options.custom_gcs_temp_location.get(),
            )
        )

    # Run the pipeline
    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
