This repo includes Terraform and a GitHub Actions workflow to deploy an AWS Glue Python shell job.

Required GitHub repository secrets:
- `AWS_ACCESS_KEY_ID` — AWS IAM key with permissions to create S3, IAM, and Glue resources
- `AWS_SECRET_ACCESS_KEY` — corresponding secret
- `AWS_REGION` — AWS region (e.g. `us-east-1`)
- `GLUE_JOB_NAME` — desired Glue job name
- `GLUE_IAM_ROLE_NAME` — IAM role name for Glue
- `SCRIPT_BUCKET_PREFIX` — prefix for the S3 bucket name (workflow will append a short id)
- `GLUE_VERSION` — (optional) Glue version, e.g. `3.0`

Usage: push to `main` branch and the workflow will run `terraform init` and `terraform apply`.

Notes:
- The workflow uploads `awsglue.py` (located at repository root) to the created S3 bucket and creates the Glue job referencing that script.
- Adjust IAM policies in `terraform/main.tf` to fit least-privilege requirements for production.
