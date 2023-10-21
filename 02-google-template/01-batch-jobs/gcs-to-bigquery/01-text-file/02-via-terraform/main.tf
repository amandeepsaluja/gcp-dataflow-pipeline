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
