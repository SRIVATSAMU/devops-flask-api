# DevOps REST API Project

A Python Flask REST API deployed using Docker and Docker Compose.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Git and GitHub

## API Endpoints

| Endpoint | Description |
|---|---|
| / | Application information |
| /health | Health check |
| /api/status | Application status |

## Run Locally

Install dependencies:

    pip install -r app/requirements.txt

Start the application:

    python app/main.py

## Run with Docker Compose

    docker compose up -d --build

Access the application:

    http://localhost:5000/

Health check:

    http://localhost:5000/health

Stop the application:

    docker compose down
