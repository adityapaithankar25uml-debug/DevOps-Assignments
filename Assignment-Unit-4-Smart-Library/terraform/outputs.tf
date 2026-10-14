output "vpc_id" {
  description = "ID of the Smart Library VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "security_group_id" {
  description = "ID of the application security group"
  value       = aws_security_group.app.id
}

output "instance_id" {
  description = "ID of the application EC2 instance"
  value       = aws_instance.app.id
}

output "instance_public_ip" {
  description = "Public IPv4 address of the application server"
  value       = aws_instance.app.public_ip
}

output "backup_bucket_name" {
  description = "Name of the private, encrypted backup bucket"
  value       = aws_s3_bucket.backups.bucket
}

output "application_url" {
  description = "HTTP URL for the application after Nginx is configured"
  value       = "http://${aws_instance.app.public_ip}"
}
