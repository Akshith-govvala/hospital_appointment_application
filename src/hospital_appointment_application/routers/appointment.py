from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from hospital_appointment_application.database import get_db
from hospital_appointment_application.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
)
from hospital_appointment_application.services.appointment_service import (
    create_appointment,
    get_appointment,
    get_appointments,
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"],
)


@router.get("", response_model=list[AppointmentResponse])
def read_appointments(db: Session = Depends(get_db)):
    return get_appointments(db)


@router.post(
    "",
    response_model=AppointmentResponse,
    status_code=201,
)
def add_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
):
    return create_appointment(db, appointment)


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse,
)
def read_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
):
    appointment = get_appointment(
        db,
        appointment_id,
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found",
        )

    return appointment