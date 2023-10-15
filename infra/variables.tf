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

variable "docker_address" {
  type        = string
  description = "Docker registry address"
  default     = "us-central1-docker.pkg.dev"
}

variable "docker_username" {
  type        = string
  description = "Docker registry username"
  default     = "oauth2accesstoken"
}

variable "docker_path" {
  type        = string
  description = "Docker registry path"
  default     = "dataflow-templates"
}

variable "docker_image_name" {
  type        = string
  description = "Docker image name"
  default     = "gar-template"
}

variable "docker_image_tag" {
  type        = string
  description = "Docker image tag"
  default     = "latest"
}

variable "gcp_auth_token" {
}
