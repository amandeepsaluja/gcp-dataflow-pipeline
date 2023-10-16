# GCP Dataflow Pipeline

## Overview

In this project, we will build a data pipeline using Google Cloud Platform's Dataflow service. We will be creating a custom Flex template to run a data pipeline that will read data from API, perform some transformations on the data, and write the results to a BigQuery table. We will then use the Dataflow service to run the pipeline.

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

## Project Steps

### 1. Create Apache Beam Pipeline (Flex Template)

In this step, we will be creating the apache beam pipeline that will be used to read data from an FPL API, perform some transformations on the data, and write the results to a BigQuery table. The pipeline will be created in the `pipeline.py` file.

### 2. Setup Terraform

In this step, we will be setting up Terraform to create the infrastructure needed to run the pipeline.The Terraform code will be written in the `main.tf` file.

### 3. Create and Deploy Docker Image of the Flex Template on Artifact Registry

In this step, we will be creating a Docker image that will be used to run the pipeline. The Docker image will be created in the `Dockerfile` file. We will then deploy the Docker image to Artifact Registry.

##### References

- https://cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#setting_required_dockerfile_environment_variables
- https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build
- https://cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run
- https://xebia.com/blog/a-declarative-approach-for-dataflow-flex-templates/
- https://cloud.google.com/blog/topics/developers-practitioners/why-you-should-be-using-flex-templates-your-dataflow-deployments
- https://medium.com/google-cloud/ci-cd-for-dataflow-java-with-flex-templates-and-cloud-build-e3c584b8e564
