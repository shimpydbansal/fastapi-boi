# import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_handle_health():
    """Test the health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Ok!"}
