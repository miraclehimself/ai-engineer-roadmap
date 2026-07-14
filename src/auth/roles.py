from fastapi import HTTPException

def require_role(current_user: dict, required_role: str):

    if current_user['role'] != required_role:
        raise HTTPException(
            status_code=403,
            details="You do not have permission to perform this action"
        )