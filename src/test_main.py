# import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_handle_question():
    """Test the handle_question endpoint"""
    response = client.get("/question-answering?question=What is the capital of France?")
    assert response.status_code == 200
    assert response.json() == {
        "question": "What is the capital of France?",
        "answer": "Answer to the question",
    }
