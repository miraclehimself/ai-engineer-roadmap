from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.jwt_handler import decode_access_token

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )
    
    return payload

def admin_required(
    current_user=Depends(get_current_user),
):
    if current_user.get("role").lower() != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )
    return current_user
  

