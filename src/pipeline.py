import argparse
import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions


class ExtractFields(beam.DoFn):
    def process(self, element):
        from datetime import datetime

        # Extract the required fields
        event = element["event"]  # gameweek

        kickoff_time_str = element["kickoff_time"]
        kickoff_time = datetime.fromisoformat(kickoff_time_str.rstrip("Z"))

        started = element["started"]
        team_h = element["team_h"]
        team_a = element["team_a"]

        yield {
            "event": event,
            "kickoff_time": kickoff_time,
            "started": started,
            "team_h": team_h,
            "team_a": team_a,
        }


def run():
    import requests

    parser = argparse.ArgumentParser()

    # # Set the required arguments
    # parser.add_argument(
    #     "--project", default="gcp-practice-project-aman", help="GCP Project ID"
    # )
    # parser.add_argument(
    #     "--region", default="us-central1", help="Region of Dataflow job"
    # )
    parser.add_argument(
        "--api_endpoint", help="API Endpoint for the data", required=True
    )
    # parser.add_argument("--runner",
    #                     default="DirectRunner",
    #                     help="Runner for the pipeline")
    # parser.add_argument("--job_name", help="Name of the job", required=True)
    parser.add_argument(
        "--temp_location",
        default="gs://dataflow-bucket-gcp-practice-project-aman/temp",
        help="GCS Temp location for Dataflow",
    )
    parser.add_argument("--dataset", help="BigQuery Dataset", required=True)
    parser.add_argument("--table", help="BigQuery Table", required=True)
    parser.add_argument("--schema", help="BigQuery Schema", required=True)

    args, beam_args = parser.parse_known_args()
    beam_options = PipelineOptions(beam_args)

    with beam.Pipeline(options=beam_options) as p:
        json_data = (
            p
            | "Read API" >> beam.Create([args.api_endpoint])
            | "HTTP GET" >> beam.ParDo(lambda url: requests.get(url).json())
            | "Extract Fields" >> beam.ParDo(ExtractFields())
            | "Write to BigQuery"
            >> beam.io.WriteToBigQuery(
                table=args.table,
                dataset=args.dataset,
                schema=args.schema,
                # project=args.project,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                custom_gcs_temp_location=args.temp_location,
            )
        )

    # Run the pipeline
    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
