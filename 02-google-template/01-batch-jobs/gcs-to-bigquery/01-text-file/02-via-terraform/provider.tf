provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket = "gcp-practice-project-aman-terraform-state-bucket"
    prefix = "dataflow/google-templates"
  }
}
