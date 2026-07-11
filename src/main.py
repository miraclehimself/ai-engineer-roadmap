from fastapi import FastAPI
from src.routes.patient import router as patient_router
from src.routes.system import router as system_router
from src.database.setup import create_tables
from src.routes.auth import router as auth_router

app =FastAPI(
    title="AI Engineer Roadmap API" 
)
create_tables()

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
app.include_router(system_router)
app.include_router(auth_router)
