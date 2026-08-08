from src.database.connection import get_connection
from src.database.models.patient import PatientModel
from src.database.session import SessionLocal

def insert_patient(patient_data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO patients (id, name, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_data["id"],
            patient_data["name"],
            patient_data["status"],
            patient_data["created_at"],
            patient_data["updated_at"],
        )
    )

    connection.commit()
    connection.close()

def get_patient(patient_id: str):
    session = SessionLocal()

    try:
        patient = (
            session.query(PatientModel)
            .filter(PatientModel.id == patient_id)
            .first()
        )

        if patient is None:
            return None

        return {
            "id": patient.id,
            "name": patient.name,
            "status": patient.status,
            "created_at": patient.created_at,
            "updated_at": patient.updated_at,
        }

    finally:
        session.close()


   
def search_patients(status: str | None = None):
    session = SessionLocal()

    try:
        query = session.query(PatientModel)

        if status:
            query = query.filter(PatientModel.status == status)

        patients = query.all()

        return [
            {
                "id": patient.id,
                "name": patient.name,
                "status": patient.status,
                "created_at": patient.created_at,
                "updated_at": patient.updated_at,
            }
            for patient in patients
        ]

    finally:
        session.close()

def update_patient (patient_id: str, updated_data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE patients
        SET name = ?, status = ?, updated_at = ?
        WHERE id = ?
        """,
        (
            updated_data["name"],
            updated_data["status"],
            updated_data["updated_at"],
            patient_id
        )
    )

    connection.commit()
    connection.close()

def delete_patient(patient_id: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
      """
      DELETE FROM patients
      WHERE id = ?
      """,
      (patient_id,)
    )

    connection.commit()
    connection.close()


def get_patients(
    page: int = 1,
    size: int = 10,
    sort: str = "created_at",
):
    session = SessionLocal()

    try:
        allowed_sort_fields = {
            "id": PatientModel.id,
            "name": PatientModel.name,
            "status": PatientModel.status,
            "created_at": PatientModel.created_at,
            "updated_at": PatientModel.updated_at,
        }

        sort_column = allowed_sort_fields.get(
            sort,
            PatientModel.created_at,
        )

        sort_column = allowed_sort_fields.get(
            sort,
            PatientModel.created_at,
        )
        offset = (page - 1) * size

        patients = (
            session.query(PatientModel)
            .order_by(sort_column)
            .offset(offset)
            .limit(size)
            .all()
        )

        return [
            {
                "id": patient.id,
                "name": patient.name,
                "status": patient.status,
                "created_at": patient.created_at,
                "updated_at": patient.updated_at,
            }
            for patient in patients
        ]

    finally:
        session.close()


def count_patients():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM patients")

    result = cursor.fetchone()

    connection.close()

    return result["total"]
