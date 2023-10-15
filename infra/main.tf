provider "docker" {

  alias = "gcr_provider"

  registry_auth {

    address  = var.docker_address
    username = var.docker_username
    password = var.gcp_auth_token # comes from GitHub Actions

  }
}

resource "docker_registry_image" "dataflow_image" {

  provider      = docker.gcr_provider
  name          = docker_image.image.name
  keep_remotely = true

}

resource "docker_image" "image" {

  provider = docker.gcr_provider

  name = "${var.docker_address}/${var.project_id}/${var.docker_path}/${var.docker_image_name}:${var.docker_image_tag}"

  build {
    context    = "${path.cwd}/infra"
    dockerfile = "Dockerfile" # file in infra/

  }
}
