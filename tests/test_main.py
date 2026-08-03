from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_active_patient():

    patient_data = {
        "id": "13001",
        "name": "Test Patient",
        "status": "Active"
    }

    # Create the patient if it doesn't already exist.
    create_response = client.post(
        "/patient",
        json=patient_data
    )

    # Allow either:
    # 200 = newly created
    # 409 = already exists
    assert create_response.status_code in [200, 409]

    response = client.get("/patient/13001")

    assert response.status_code == 200

    data = response.json()

    assert data["valid"] is True
    assert data["data"]["id"] == "13001"
    assert data["data"]["status"] == "Active"


def test_patient_not_found():
    response = client.get("/patient/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"