from fastapi import FastAPI

from hospital_appointment_application.routers.appointment import (
    router as appointment_router,
)
from hospital_appointment_application.routers.doctor import router as doctor_router
from hospital_appointment_application.routers.patient import router as patient_router

app = FastAPI(title="Hospital Appointment API")

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)