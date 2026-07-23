from fastapi import FastAPI
from src.routes.patient import router as patient_router
from src.routes.system import router as system_router
from src.database.setup import create_tables
from src.routes.auth import router as auth_router
from fastapi import Request
from fastapi.responses import JSONResponse
from src.exceptions.patient_exceptions import PatientNotFoundException
import time

from src.core.logging import logger



app =FastAPI(
    title="AI Engineer Roadmap API" 
)

create_tables()

@app.middleware("http")
async def log_requests(request: Request, call_next):
     start_time = time.time()

     response = await call_next(request)

     process_time = (time.time() - start_time) * 1000

     logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{request.status_code} "
        f"{process_time:.2f}ms"
     )

     return response

@app.exception_handler(PatientNotFoundException)
async def patient_not_found_exception_handler(
        request: Request,
        exc: PatientNotFoundException,
):
        return JSONResponse(
             status_code=404,
             content={
                  "valid": False,
                  "message": str(exc),
             },
        )






@app.get("/health")
def health_check():
    logger.info("Health endpoint called")
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
