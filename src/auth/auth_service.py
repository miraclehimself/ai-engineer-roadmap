import sqlite3

from src.auth.jwt_handler import create_access_token
from src.auth.security import hash_password, verify_password
from src.database.user_repository import (
    create_user,
    get_user_by_username,
)
from src.models.user import UserCreate, UserInDB


def login(username: str, password: str) -> dict | None:
    user = get_user_by_username(username)

    if user is None:
        return None

    if not user.is_active:
        return None

    if not verify_password(
        password,
        user.hashed_password,
    ):
        return None

    access_token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


def register_user(user_data: UserCreate) -> UserInDB | None:
    existing_user = get_user_by_username(user_data.username)

    if existing_user is not None:
        return None

    hashed_password = hash_password(user_data.password)

    try:
        return create_user(
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
            role=user_data.role,
        )
    except sqlite3.IntegrityError:
        return None
    