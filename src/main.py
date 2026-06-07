from fastapi import FastAPI
from src.routes.patient import router as patient_router

app =FastAPI(
    title="AI Engineer Roadmap API" 
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-engineer-roadmap-api"
    }

app.include_router(patient_router)
