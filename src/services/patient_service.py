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
    
    if patient_id == "99999":
        return {
        "valid": False,
        "message": "Patient not found",
    }
    
    status = "Inactive"

    if patient_id == "77777":
        status = "Active"

    return {
        "valid": True,
        "patient": {
            "id": patient_id,
            "name": f"Patient {patient_id}",
            "status": status
        }
    }