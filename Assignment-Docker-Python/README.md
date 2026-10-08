# Dockerizing a Python App

## Aim
To containerize a simple Flask web application using Docker.

## Technologies
- Python 3.9
- Flask 2.3.2
- Werkzeug 2.3.6
- Docker

## Project Files
- `app.py` - Flask web application.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - Instructions to build the Docker image.

## Build the Docker Image
```bash
sudo docker build -t my-python-app .
