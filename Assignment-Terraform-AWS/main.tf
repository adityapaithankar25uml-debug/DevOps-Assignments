
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "test_bucket" {
  bucket        = "nested-tf-bucket-${random_id.bucket_suffix.hex}"
  force_destroy = true

  tags = {
    CreatedBy   = "EC2-Terraform-Runner"
    Environment = "Nested-Lab"
  }
}

output "created_bucket_name" {
  value = aws_s3_bucket.test_bucket.bucket
}

