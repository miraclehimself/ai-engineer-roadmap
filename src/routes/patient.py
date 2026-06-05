from fastapi import APIRouter
from src.services.patient_service import validate_patient

router = APIRouter()

@router.get("/patient/{patient_id}")
def get_patient(patient_id: str):

    result = validate_patient(patient_id)

    return result