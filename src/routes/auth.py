from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.auth.auth_service import login

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(credentials: LoginRequest):
    
    result = login(
        credentials.username,
        credentials.password
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    return result