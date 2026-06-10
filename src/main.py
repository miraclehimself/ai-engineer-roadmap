from fastapi import FastAPI
from src.routes.patient import router as patient_router

app =FastAPI(
    title="AI Engineer Roadmap API" 
)

@app.get("/health")
def health_check():
    print ("Health endpoint called")
    return {
        "status": "healthy",
        "service": "ai-engineer-roadmap-api"
    }

@app.get("/info")
def get_info():
    return {
        "system": "AI Engineer Roadmap",
        "version":"1.0",
        "environment": "development"
    }
    

app.include_router(patient_router)
