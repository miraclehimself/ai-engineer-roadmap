from sqlalchemy.orm import Session

from src.database.models.patient import PatientModel

def get_patient(session: Session, patient_id: str):

    return (
        session.query(PatientModel)
        .filter_by(id=patient_id)
        .first()
    )

