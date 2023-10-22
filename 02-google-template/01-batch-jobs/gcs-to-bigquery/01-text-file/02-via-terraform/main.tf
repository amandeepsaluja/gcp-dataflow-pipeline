# upload files to cloud storage
resource "google_storage_bucket_object" "js_file" {
  name   = "${var.gcs_folder_location}${var.js_file_source}"
  source = var.js_file_source
  bucket = var.gcs_bucket_name
}

resource "google_storage_bucket_object" "sample_data" {
  name   = "${var.gcs_folder_location}${var.sample_data_source}"
  source = var.sample_data_source
  bucket = var.gcs_bucket_name
}

resource "google_storage_bucket_object" "bq_schema" {
  name   = "${var.gcs_folder_location}${var.bq_schema_source}"
  source = var.bq_schema_source
  bucket = var.gcs_bucket_name
}

# create dataflow job
resource "google_dataflow_job" "gcs_to_bq" {
  name              = var.google_dataflow_job
  template_gcs_path = var.dataflow_template_source
  temp_gcs_location = "gs://${var.gcs_bucket_name}/temp"
  region            = var.region

  parameters = {
    javascriptTextTransformFunctionName = var.js_function_name
    JSONPath                            = "gs://${var.gcs_bucket_name}/${var.gcs_folder_location}${var.bq_schema_source}"
    javascriptTextTransformGcsPath      = "gs://${var.gcs_bucket_name}/${var.gcs_folder_location}${var.sample_data_source}"
    inputFilePattern                    = "gs://${var.gcs_bucket_name}/${var.gcs_folder_location}${var.sample_data_source}"
    outputTable                         = var.bq_table_name
    bigQueryLoadingTemporaryDirectory   = "gs://${var.gcs_bucket_name}/temp"
  }
}
