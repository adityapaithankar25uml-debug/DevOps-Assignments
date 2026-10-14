# Smart Library Management Platform

A cloud-hosted library management application deployed using Docker,
Terraform, Ansible, Nginx, and Amazon S3.

## Student Details

- Name: Aditya Viresh Paithankar
- Course: B.Tech CSE (AI & ML)
- Year: Second Year
- University: Sanjivani University

## Project Overview

The Smart Library Management Platform provides a web interface for
managing a library's book collection and tracking book availability.

The application is built with Python Flask and SQLite. Docker
containerizes the application, Terraform provisions AWS infrastructure,
and Ansible automates application deployment and Nginx configuration.

Automated database backups are uploaded to Amazon S3.

## Features

- Library dashboard with total, available, and borrowed book counts.
- Book collection and search interface.
- Add books to the collection.
- Borrow and return books.
- SQLite database persistence.
- Containerized deployment using Docker.
- Infrastructure provisioning using Terraform.
- Automated deployment using Ansible.
- Nginx reverse proxy.
- Automated SQLite database backups to Amazon S3.
- S3 bucket versioning and server-side encryption.

## Technology Stack

- Python and Flask
- SQLite
- HTML and CSS
- Docker
- AWS EC2
- Amazon S3
- Terraform
- Ansible
- Nginx
- Ubuntu Linux

## Project Structure

```text
Assignment-Unit-4-Smart-Library/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── versions.tf
│   ├── iam.tf
│   └── .terraform.lock.hcl
├── ansible/
│   ├── deploy.yml
│   ├── deploy-app.yml
│   ├── inventory.ini
│   └── smart-library-nginx.conf
├── docs/
└── screenshots/
