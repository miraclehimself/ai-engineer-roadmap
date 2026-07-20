from src.models.patient import Patient
from src.data.patient_db import patients
from  datetime import datetime
from src.services.audit_service import log_action
from src.data.storage import save_patients
from src.database.patient_respository import count_patients, insert_patient, get_patient, search_patients as search_patients_from_db, update_patient as update_patient_in_db, delete_patient as delete_patient_from_db, get_patients as get_patients_from_db
from src.exceptions.patient_exceptions import PatientNotFoundException




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
    
    database_patient = get_patient(patient_id)
    
    if database_patient is None:
        return {
            "valid": False,
            "message": "Patient not found",
        }
    
    
    return {
        "valid": True,
        "patient":{
            "id": database_patient["id"],
            "name": database_patient["name"],
            "status": database_patient["status"],
            "created_at": database_patient["created_at"],
            "updated_at": database_patient["updated_at"]
        }
    }
    

def search_patients_by_status(status):
    database_patients = search_patients_from_db(status)

    results = []

    for patient in database_patients:
        results.append({
                "id": patient["id"],
                "name": patient["name"],
                "status": patient["status"],
                "created_at": patient["created_at"],
                "updated_at": patient["updated_at"]
        })
        
    return results

def delete_patient(patient_id):

    if patient_id not in patients:
        raise PatientNotFoundException(patient_id)
    
    deleted = patients.pop(patient_id)
    delete_patient_from_db(patient_id)
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
    update_patient_in_db(patient_id, patients[patient_id])
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
    now = datetime.now().isoformat()
    patients[patient.id] = {
        "name": patient.name,
        "status": patient.status,
        "created_at": now,
        "updated_at": now

    }
    save_patients(patients)
    insert_patient({
        "id": patient.id,
        "name": patient.name,
        "status": patient.status,
        "created_at": now,
        "updated_at": now
    })

    log_action("CREATE", patient.id)

    return {
        "valid": True,
        "message": "Patient created successfully",
        "patient": {
            "id": patient.id,
            "name": patient.name,
            "status": patient.status, 
            "created_at": patients[patient.id].get("created_at"),
            "updated_at": patients[patient.id].get("updated_at")
        }
    }


def get_patients(page=1, size=10):

    database_patients = get_patients_from_db(page, size)
    total = count_patients()

    results = []
    for patient in database_patients:
        results.append({
            "id": patient["id"],
            "name": patient["name"],
            "status": patient["status"],
            "created_at": patient["created_at"],
            "updated_at": patient["updated_at"]
        })

    return {
        "total": total,
        "patients": results
    }