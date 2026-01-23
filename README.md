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

## 🧪 Running Tests

Automated tests are integrated into the CI pipeline and are implemented using
**pytest** to validate the basic functionality of the API.

### Run tests locally
```bash
pytest
```

## ⚙️ CI/CD Workflow (GitHub Actions)

This project uses **GitHub Actions** to implement a Continuous Integration (CI)
pipeline that runs on every push to the main branch. Changes to documentation
files (such as the README) are excluded from triggering the workflow.

### CI Pipeline Steps
1. Checkout the repository
2. Install application dependencies
3. Run automated tests using **pytest**
4. Build the Docker image
5. Scan the container image using **Trivy (Aqua Security)** to identify
   potential vulnerabilities
6. Retag and push the Docker image to **Docker Hub**

This workflow ensures that code changes are automatically validated and that
only tested, scanned, and buildable artifacts are produced. To more information you can go to the path:
[Click to see the CI stage](.github/workflows/CI.yml)














