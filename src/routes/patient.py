from fastapi import APIRouter, HTTPException
from src.services.patient_service import validate_patient, search_patients_by_status

router = APIRouter()


@router.get("/patients/search")
def search_patients(status: str | None = None):

        results = search_patients_by_status(status)

        return {
            "count": len(results),
            "results": results
            
        }

@router.get("/patient/{patient_id}")
def get_patient(patient_id: str):

    result = validate_patient(patient_id)

    if result["valid"] is False:

        if result ["message"] == "Patient not found":
            raise HTTPException(
                status_code=404, 
                detail=result["message"]
            )
    
        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )
    
    return result
