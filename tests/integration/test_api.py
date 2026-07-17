import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPI:
    
    def test_health_endpoint(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "mobilefacenet-service"
        assert data["model"] is not None
    
    def test_verify_endpoint_invalid_url(self):
        payload = {
            "reference_url": "https://invalid.url/image.jpg",
            "selfie_url": "https://invalid.url/image.jpg"
        }
        response = client.post("/api/v1/verify", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False