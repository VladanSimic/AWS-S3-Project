# AWS S3 Upload Project

This project demonstrates how to upload files to an AWS S3 bucket using Python and the boto3 library, with integration via GitHub Actions for automated uploads.

## Features

- Upload files to an S3 bucket locally using a Python script.
- Automate uploads on push to the `master` branch via GitHub Actions.
- Secure management of AWS credentials using GitHub Secrets.

## Prerequisites

- Python 3.x installed locally
- AWS account with S3 bucket created
- AWS IAM user with proper S3 permissions
- GitHub repository with configured Secrets for AWS credentials

## Setup and Usage

### 1. Configure AWS Credentials Locally

Set your AWS credentials as environment variables in your terminal before running the Python script:

