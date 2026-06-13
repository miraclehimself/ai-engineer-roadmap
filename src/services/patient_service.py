from src.models.patient import Patient
def validate_patient(patient_id):

    patients = {
        "77777": {
            "name": "John Smith",
            "status": "Active"
        },
        "88888": {
            "name": "Sarah Johns",
            "status": "Discharged"
        }
    }

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

    patients = {
        "77777": {
            "name": "John Smith",
            "status": "Active"
        },
        "88888": {
            "name": "Sarah Johns",
            "status": "Discharged"
        }
    }

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

    patients = {
        "77777": {
            "name": "John Smith",
            "status": "Active"

        },
        "88888": {
            "name": "Sarah Johns",
            "status": "Discharged"

        }
    }

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