from src.services.audit_service import audit_logs
from src.models.response import StandardResponse
from fastapi import APIRouter, HTTPException
from src.services.patient_service import (
     validate_patient,
     search_patients_by_status,
     delete_patient,
     update_patient,
     create_patient_record
)

from src.models.patient import Patient

router = APIRouter()


@router.get("/patients/search", response_model=StandardResponse)
def search_patients(status: str | None = None):

        results = search_patients_by_status(status)

        return StandardResponse(
          valid=True,
          message="Patients search completed",
          data={
               "count": len(results),
               "result": results
          }
            
        )

@router.get("/patient/{patient_id}", response_model=StandardResponse)
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
    
    return StandardResponse(
         valid=result["valid"],
         message="patient found",
         data=result["patient"]
    )

@router.post("/patient", response_model=StandardResponse)
def create_patient(patient: Patient):

    result = create_patient_record(patient)

    return StandardResponse(
         valid=result["valid"],
         message=result["message"],
         data=result["patient"]
    )

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

@router.get("/audit")
def get_audit_logs(patient_id: str | None = None):

     if patient_id:
          filtered_logs = [
               log for log in  audit_logs
               if log["patient_id"] == patient_id
          ]

          return {
               "count": len(filtered_logs),
               "logs": filtered_logs
          }
     
     return {
          "count": len(audit_logs),
          "logs": audit_logs
     }