from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from hospital_appointment_application.database import get_db
from hospital_appointment_application.schemas.doctor import (
    DoctorCreate,
    DoctorResponse,
)
from hospital_appointment_application.services.doctor_service import (
    create_doctor,
    get_doctor,
    get_doctors,
)

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("", response_model=list[DoctorResponse])
def read_doctors(db: Session = Depends(get_db)):
    return get_doctors(db)


@router.post(
    "",
    response_model=DoctorResponse,
    status_code=201,
)
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
):
    return create_doctor(db, doctor)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def read_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    doctor = get_doctor(db, doctor_id)

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found",
        )

    return doctor