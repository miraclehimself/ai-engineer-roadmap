from src.models.patient import Patient
from src.data.patient_db import patients
from  datetime import datetime

def validate_patient(patient_id):


    if not patient_id:
        return {
            "valid": False,
            "message": "Patient ID required",
        }
    
    if not patient_id.isdigit():
        return {
            "valid": False,
            "message": "Patient ID must contain numbers only",
        }
    
    if patient_id not in patients:
        return {
            "valid": False,
            "message": "Patient not found",
        }
    
    patient = patients[patient_id]
    
    
    return {
        "valid": True,
        "patient": Patient(
            id=patient_id,
            name=patient["name"],
            status=patient["status"]
        )
    }

def search_patients_by_status(status):

    results = []
    for patient_id, patient in patients.items():
        if status is None or patient["status"] == status:
        
            results.append({
                "id": patient_id,
                "name": patient["name"],
                "status": patient["status"]
            })
    return results

def delete_patient(patient_id):

    if patient_id not in patients:
        return {
            "valid": False,
            "message": "Patient not found"

        }
    
    deleted = patients.pop(patient_id)

    return {
        "valid": True,
        "message": "Patient deleted",
        "patient": deleted
    }

def update_patient(patient_id, updated_data):

    if patient_id not in patients:
        return {
            "valid": False,
            "message": "Patient not found"

        }
    patients[patient_id].update(updated_data)

    return {
        "valid": True,
        "message": "Patient updated",
        "patient": patients[patient_id]
    }
def create_patient_record(patient):
    if patient.id in patients:
        return {
            "valid": False,
            "message": "Patient already exists"

    }

    patients[patient.id] = {
        "name": patient.name,
        "status": patient.status,
        "created_at": datetime.now().isoformat()
    }

    return {
        "valid": True,
        "message": "Patient created successfully",
        "patient": {
            "id": patient.id,
            "name": patient.name,
            "status": patient.status
        }
    }