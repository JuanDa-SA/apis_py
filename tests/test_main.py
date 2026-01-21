from fastapi.testclient import TestClient
from app.main import app
import time
import pytest


@pytest.fixture
def client():
    return TestClient(app)


def test_hello_endpoint(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello PSL group"}


@pytest.mark.performance
def test_health_performance(client):
    start = time.time()
    response = client.get("/health")
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 1.0


@pytest.mark.parametrize(
    "endpoint, expected_status",
    [
        ("/hello", 200),
        ("/health", 200),
        ("/not-found", 404),
    ]
)
def test_endpoints_status(client, endpoint, expected_status):
    response = client.get(endpoint)
    assert response.status_code == expected_status



