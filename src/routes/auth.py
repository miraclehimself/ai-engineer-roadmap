from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.auth_service import login
from fastapi import Depends
from src.auth.dependencies import get_current_user


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

@router.get("/me")
def me(current_user: dict = Depends(get_current_user)):
    
    return {
        "username": current_user["sub"],
        "role": current_user["role"]
    }