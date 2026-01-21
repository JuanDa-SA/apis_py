from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello PSL group"}

@app.get("/health", summary="Perform a health check", response_description="Status of the service")
def health_check():
    """
    Perform a health check.

    Returns:
        A dictionary with the service status.
    """
    return {"status": "Healthy"}
