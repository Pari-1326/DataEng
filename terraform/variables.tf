variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "bucket_prefix" {
  description = "Prefix for the S3 bucket that will store Glue scripts"
  type        = string
  default     = "dataeng-glue-scripts"
}

variable "script_key" {
  description = "S3 key (filename) for the uploaded Glue script"
  type        = string
  default     = "awsglue.py"
}

variable "job_name" {
  description = "Name of the Glue job"
  type        = string
  default     = "dataeng-glue-job"
}

variable "iam_role_name" {
  description = "IAM role name for Glue"
  type        = string
  default     = "dataeng-glue-role"
}

variable "glue_version" {
  description = "Glue version to use (e.g., 2.0, 3.0)"
  type        = string
  default     = "3.0"
}
