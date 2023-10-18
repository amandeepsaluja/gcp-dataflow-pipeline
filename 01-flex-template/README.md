# Dataflow Flex Template Pipeline

## Overview

In this project, we will build a data pipeline using Google Cloud Platform's Dataflow service. We will be creating a custom Flex template to run a data pipeline that will read data from API, perform some transformations on the data, and write the results to a BigQuery table. We will then use the Dataflow service to run the pipeline.

## Medium Articles

- [GCP Dataflow Flex Template Pipeline — Part 1 (Overview)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-1-overview-b1ae8151e93d)
- [GCP Dataflow Flex Template Pipeline — Part 2 (Local Testing)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-2-local-development-5c3bf32923c3)
- [GCP Dataflow Flex Template Pipeline — Part 3 (Pipeline Development)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-3-pipeline-development-708b445bb29f)
- [GCP Dataflow Flex Template Pipeline — Part 4 (Docker & Terraform Setup)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-3-docker-terraform-setup-a1c671644068)
- [GCP Dataflow Flex Template Pipeline — Part 5 (GitHub Actions Setup for Deployment)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-5-github-actions-setup-for-deployment-2b62ac7940f2)
- [GCP Dataflow Flex Template Pipeline — Part 6 (Troubleshooting)](https://medium.com/@saluja.amandeep/gcp-dataflow-flex-template-pipeline-part-6-troubleshooting-258aca620350)

## Pre-requisites

- [ ] Workload Identity Federation (used to authenticate with GCP services via GitHub Actions)

## Technologies Used

- Google Cloud Platform
  - BigQuery
  - Cloud Storage
  - Cloud Dataflow
  - Workload Identity Federation
- Python
- Terraform
- GitHub Actions
- Docker

## Repository Structure

```
📦01-flex-template
 ┣ 📂docker
 ┃ ┗ 📜Dockerfile
 ┣ 📂infra
 ┃ ┣ 📜main.tf
 ┃ ┣ 📜providers.tf
 ┃ ┗ 📜variables.tf
 ┣ 📂src
 ┃ ┣ 📜pipeline.py
 ┃ ┣ 📜requirements.txt
```

## Project Steps

### 1. Create Apache Beam Pipeline (Flex Template)

In this step, we will be creating the apache beam pipeline that will be used to read data from an FPL API, perform some transformations on the data, and write the results to a BigQuery table. The pipeline will be created in the `pipeline.py` file.

### 2. Setup Terraform

In this step, we will be setting up Terraform to create the infrastructure needed to run the pipeline.The Terraform code will be written in the `main.tf` file.

### 3. Create and Deploy Docker Image of the Flex Template on Artifact Registry

In this step, we will be creating a Docker image that will be used to run the pipeline. The Docker image will be created in the `Dockerfile` file. We will then deploy the Docker image to Artifact Registry.

### 4. Create and Deploy Flex Template Job via GitHub Actions

In this step, we will be creating a GitHub Action that will be used to deploy the Flex Template Job to Dataflow. The GitHub Action will be created in the `.github/workflows/deploy-dataflow-template.yml` file.

## Issues I Faced (WIP to make it more descriptive)

- Flags in Parameters in GitHub Actions
- Docker build error due to path issues
- Context in Terraform

## References

- https://cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#setting_required_dockerfile_environment_variables
- https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build
- https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run
- https://xebia.com/blog/a-declarative-approach-for-dataflow-flex-templates/
- https://cloud.google.com/blog/topics/developers-practitioners/why-you-should-be-using-flex-templates-your-dataflow-deployments
- https://medium.com/google-cloud/ci-cd-for-dataflow-java-with-flex-templates-and-cloud-build-e3c584b8e564
