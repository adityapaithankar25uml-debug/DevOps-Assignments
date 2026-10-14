# Deployment Guide

## Architecture

The Smart Library Management Platform runs on AWS EC2. Nginx receives HTTP
requests and forwards them to the Flask application running through Gunicorn
inside Docker. SQLite stores the library data in a persistent host directory.

Terraform provisions AWS infrastructure, and Ansible configures the server
and deploys the application.

## Prerequisites

- AWS CLI configured with appropriate permissions
- Terraform
- Ansible
- SSH access to the target EC2 instance
- Docker on the target server

## Terraform

Run these commands from the terraform directory:

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan
```

## Automated SQLite Backups

The application database is stored on the EC2 host at
`/opt/smart-library/data/library.db`. The backup script creates a
consistent SQLite backup, verifies its integrity, and uploads it to
the project's Amazon S3 bucket.

### Schedule and Logging

The cron schedule is configured in `/etc/cron.d/smart-library-backup`.
It runs every 10 minutes:

```cron
*/10 * * * * root /usr/local/bin/smart-library-backup.sh >> /var/log/smart-library-backup.log 2>&1
```

Check the scheduler and recent backup results:

```bash
sudo systemctl is-active cron
sudo tail -n 30 /var/log/smart-library-backup.log
aws s3 ls s3://smart-library-backups-acfc2463/backups/
```

### Restore Procedure

**Caution:** Restore only after confirming the correct backup. Replacing a
live database can overwrite newer library records.

1. Download the selected backup from S3.
2. Stop the application container before replacing the live database.
3. Preserve a copy of the current database.
4. Verify the downloaded backup with SQLite's `PRAGMA integrity_check`.
5. Restore the verified database with the correct ownership and permissions.
6. Start the container and test `/health` and the library dashboard.

Example download and integrity check:

```bash
aws s3 cp \
  s3://smart-library-backups-acfc2463/backups/REPLACE_WITH_BACKUP_FILENAME.db \
  /tmp/library-restore.db

python3 - <<'PY'
import sqlite3

path = "/tmp/library-restore.db"
with sqlite3.connect(path) as connection:
    result = connection.execute("PRAGMA integrity_check").fetchone()[0]
    print(result)
    if result != "ok":
        raise SystemExit("Backup integrity check failed")
PY
```

Proceed with replacing the live database only after the integrity check
returns `ok` and the current database has been preserved.
