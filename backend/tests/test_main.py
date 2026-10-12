
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to VerwaltungsAI"
    assert response.json()["docs"] == "/docs"
    assert response.json()["health"] == "/health"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "verwaltungsai-api",
        "version": "0.1.0",
    }


def test_api_information_endpoint():
    response = client.get("/api/v1")

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "VerwaltungsAI"
    assert data["version"] == "0.1.0"
    assert "Human review required" in data["decision_policy"]
