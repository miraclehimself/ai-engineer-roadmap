from fastapi import APIRouter, HTTPException
from src.services.patient_service import (
     validate_patient,
     search_patients_by_status,
     delete_patient,
     update_patient
)

from src.models.patient import Patient

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

@router.post("/patient")
def create_patient(patient: Patient):
     
     return {
          "message": "Patient created successfully",
          "patient": patient

     }

@router.delete("/patient/{patient_id}")
def remove_patient(patient_id: str):
     
     result = delete_patient(patient_id)

     if result["valid"] is False:
          raise HTTPException(
               status_code=404,
               detail=result["message"]
          )
     return result 
     
@router.put("/patient/{patient_id}")
def edit_patient(patient_id: str, patient: Patient):
     
        result = update_patient(
             patient_id,
             patient.model_dump()
        )
        
        if result["valid"] is False:
             raise HTTPException(
                  status_code=404,
                  detail=result["message"]
             )
        return result