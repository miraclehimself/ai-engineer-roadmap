from fastapi import FastAPI
from src.routes.patient import router as patient_router

app =FastAPI(
    title="AI Engineer Roadmap API" 
)
app.include_router(patient_router)
