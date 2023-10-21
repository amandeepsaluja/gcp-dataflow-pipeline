variable "project_id" {
  type        = string
  description = "Google project ID"
  default     = "gcp-practice-project-aman"
}

variable "region" {
  type        = string
  description = "Google project region"
  default     = "us-central1"
}

variable "gcs_bucket_name" {
  type        = string
  description = "Google Cloud Storage bucket name"
  default     = "dataflow-bucket-gcp-practice-project-aman"
}

variable "gcs_folder_location" {
  type        = string
  description = "Google Cloud Storage folder location"
  default     = "02-google-template/01-batch-jobs/gcs-to-bigquery/01-text-file/02-via-terraform/"
}

variable "js_file_source" {
  type        = string
  description = "Javascript file name"
  default     = "user-function/transform.js"
}

variable "sample_data_source" {
  type        = string
  description = "Sample data file name"
  default     = "data/sample_input.csv"
}

variable "bq_schema_source" {
  type        = string
  description = "BigQuery schema file name"
  default     = "config/bq-schema.json"
}
