from datetime import datetime

from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_start: datetime
    appointment_end: datetime


class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_start: datetime
    appointment_end: datetime

    class Config:
        from_attributes = True