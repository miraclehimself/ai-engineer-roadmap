from src.models.patient import Patient
from src.data.patient_db import patients
from  datetime import datetime
from src.services.audit_service import log_action
from src.data.storage import save_patients

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
        "patient":{
            "id": patient_id,
            "name": patient["name"],
            "status": patient["status"],
            "created_at": patient.get("created_at"),
            "updated_at": patient.get("updated_at")
        }
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
    save_patients(patients)

    log_action("DELETE", patient_id)

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
    patients[patient_id]["updated_at"] = datetime.now().isoformat()
    save_patients(patients)

    log_action("UPDATE", patient_id)

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
    save_patients(patients)

    log_action("CREATE", patient.id)

    return {
        "valid": True,
        "message": "Patient created successfully",
        "patient": {
            "id": patient.id,
            "name": patient.name,
            "status": patient.status
        }
    }