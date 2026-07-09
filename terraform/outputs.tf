output "glue_job_name" {
  description = "Name of the created Glue job"
  value       = aws_glue_job.job.name
}

output "script_s3_path" {
  description = "S3 location of the uploaded script"
  value       = "s3://${aws_s3_bucket.scripts.bucket}/scripts/${var.script_key}"
}

output "glue_role_arn" {
  description = "IAM role ARN for Glue"
  value       = aws_iam_role.glue_role.arn
}

output "scripts_bucket" {
  description = "S3 bucket name storing scripts"
  value       = aws_s3_bucket.scripts.bucket
}
