from src.database.connection import get_connection

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
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, status, created_at, updated_at
        FROM patients
        WHERE id = ?
        """,
        (patient_id,)
    )

    patient = cursor.fetchone()

    connection.close()

    return patient

def search_patients(status: str = None):
    connection = get_connection()
    cursor = connection.cursor()

    if status:
        cursor.execute(
            """
            SELECT id, name, status, created_at, updated_at
            FROM patients
            WHERE status = ?
            """,
            (status,)
        )
    else:
        cursor.execute(
            """
            SELECT id, name, status, created_at, updated_at
            FROM patients
            """
        )
    
    patients = cursor.fetchall()
    
    connection.close()

    return patients

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