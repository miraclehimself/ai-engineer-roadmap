import sqlite3

from src.database.connection import get_connection
from src.models.user import UserInDB


def get_user_by_username(username: str) -> UserInDB | None:
    connection = get_connection()
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            full_name,
            hashed_password,
            role,
            is_active
        FROM users
        WHERE username = ?
        """,
        (username,),
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return UserInDB(
        id=row["id"],
        username=row["username"],
        full_name=row["full_name"],
        hashed_password=row["hashed_password"],
        role=row["role"],
        is_active=bool(row["is_active"]),
    )


def create_user(
    username: str,
    full_name: str,
    hashed_password: str,
    role: str = "user",
) -> UserInDB:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (
            username,
            full_name,
            hashed_password,
            role,
            is_active
        )
        VALUES (?, ?, ?, ?, 1)
        """,
        (
            username,
            full_name,
            hashed_password,
            role,
        ),
    )

    user_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return UserInDB(
        id=user_id,
        username=username,
        full_name=full_name,
        hashed_password=hashed_password,
        role=role,
        is_active=True,
    )