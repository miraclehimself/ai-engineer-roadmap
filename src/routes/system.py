from fastapi import APIRouter

router = APIRouter()

@router.get("/version")
def version():
    return {
        "application": "AI Engineer Roadmap API",
        "version": "1.0.0",
        "environment": "Development"
    }