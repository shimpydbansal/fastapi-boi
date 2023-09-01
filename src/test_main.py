"""Test the main module."""
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_handle_health():
    """Test the health endpoint.

    Sends a GET request to the /health endpoint and checks that the response
    status code is 200 and the response JSON contains the expected keys
    and values.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"database": True, "message": "Ok!"}
