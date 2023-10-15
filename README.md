# GCP Dataflow Pipeline

## Overview

In this project, we will build a data pipeline using Google Cloud Platform's Dataflow service. We will be creating a custom Flex template to run a data pipeline that will read data from API, perform some transformations on the data, and write the results to a BigQuery table. We will then use the Dataflow service to run the pipeline.

## Pre-requisites

- [ ] Workload Identity Federation (used to authenticate with GCP services via GitHub Actions)

## Technologies Used

- Google Cloud Platform
  - Cloud Storage
  - Cloud Dataflow
  - BigQuery
  - Workload Identity Federation
- Python
- Terraform
- GitHub Actions

## Project Steps

### 1. Create Apache Beam Pipeline

In this step, we will be creating the apache beam pipeline that will be used to read data from an FPL API, perform some transformations on the data, and write the results to a BigQuery table. The pipeline will be created in the `pipeline.py` file.
