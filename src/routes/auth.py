from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from src.auth.auth_service import login, register_user
from src.auth.dependencies import get_current_user
from src.models.user import UserCreate, UserResponse


router = APIRouter(tags=["Authentication"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(user_data: UserCreate) -> UserResponse:
    user = register_user(user_data)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )

    return UserResponse(
        id=user.id,
        username=user.username,
        full_name=user.full_name,
        role=user.role,
        is_active=user.is_active,
    )


@router.post("/login")
def login_user(credentials: LoginRequest):
    result = login(
        credentials.username,
        credentials.password,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return result


@router.get("/me")
def me(current_user: dict = Depends(get_current_user)):
    return {
        "username": current_user["sub"],
        "role": current_user["role"],
    }