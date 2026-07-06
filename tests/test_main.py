from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_active_patient():
    response = client.get("/patient/13001")

    assert response.status_code == 200
    assert response.json()["valid"] is True
    assert response.json()["data"]["status"] == "Active"

def test_patient_not_found():
    response = client.get("/patient/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"