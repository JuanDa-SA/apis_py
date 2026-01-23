## 🚀 Application Overview

This project implements a simple RESTful API built with Python, designed to demonstrate
core DevOps practices such as containerization, automated testing, CI pipelines,
Security, Testing, and Observability (STO) best practices, and Kubernetes deployments.

The service exposes the following endpoints:

- `GET /hello`  
  Returns a simple greeting message to verify that the service is reachable.

- `GET /health`  
  Returns the current health status of the application. This endpoint is intentionally
  minimal and can be used for monitoring, liveness, and readiness checks. The `/health` endpoint returns a 
  static response, as the service has no external dependencies to validate (check connections with databases, 
  check cache with Redis, etc.).


The application is built using **FastAPI** and runs as a stateless service.
Automated tests are implemented using **pytest** to validate API behavior and service
health. The service does not rely on any external databases or third-party services,
keeping the focus on infrastructure, CI/CD, and deployment workflows.


## 🏃 Running the Service Locally

### Prerequisites
- Python 3.10 or higher
- pip

### Install dependencies
```bash
pip install -r requirements.txt
```

### Command to start the application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
