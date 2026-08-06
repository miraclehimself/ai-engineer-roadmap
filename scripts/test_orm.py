from src.database.session import SessionLocal
from src.database.orm_repository import get_patient

session = SessionLocal()

try:
    patient = get_patient(session, "77787")

    if patient:
        print("ID:", patient.id)
        print("Name", patient.name)
        print("Status", patient.status)
    else:
        print("Patient not found")

finally:
    session.close()

    