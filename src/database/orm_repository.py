from sqlalchemy.orm import Session

from src.database.models.patient import PatientModel

def get_patient(
    session: Session, 
    patient_id: str
) -> PatientModel | None:

    return (
        session.query(PatientModel)
        .filter_by(id=patient_id)
        .first()
    )

