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