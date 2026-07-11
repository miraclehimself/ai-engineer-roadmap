from src.auth.users import users
from src.auth.security import verify_password
from src.auth.jwt_handler import create_access_token

def login(username: str, password: str):

    user = users.get(username)

    if not users:
        return None
    
    if not verify_password(password, user["hashed_password"]):
        return None
    
    access_token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }