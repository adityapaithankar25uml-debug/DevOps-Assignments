variable "aws_region" {
  description = "AWS region for the Smart Library deployment"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name used for AWS resource naming"
  type        = string
  default     = "smart-library"
}

variable "instance_type" {
  description = "EC2 instance type for the application server"
  type        = string
  default     = "t3.micro"
}

variable "ami_id" {
  description = "Ubuntu 24.04 AMI in ap-south-1"
  type        = string
  default     = "ami-065d2b03fb493085a"
}

variable "key_name" {
  description = "Existing EC2 key pair name"
  type        = string
  default     = "unit4-library-key"
}

variable "allowed_ssh_cidr" {
  description = "Public IPv4 CIDR allowed to SSH to the application server"
  type        = string

  validation {
    condition     = can(cidrnetmask(var.allowed_ssh_cidr)) && endswith(var.allowed_ssh_cidr, "/32")
    error_message = "Use your public IPv4 address followed by /32, for example 203.0.113.10/32."
  }
}

variable "root_volume_size" {
  description = "EC2 root volume size in GiB"
  type        = number
  default     = 12
}
