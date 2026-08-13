from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from hospital_appointment_application.database import get_db
from hospital_appointment_application.schemas.patient import (
    PatientCreate,
    PatientResponse,
)
from hospital_appointment_application.services.patient_service import (
    create_patient,
    get_patient,
    get_patients,
)

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("", response_model=list[PatientResponse])
def read_patients(db: Session = Depends(get_db)):
    return get_patients(db)


@router.post(
    "",
    response_model=PatientResponse,
    status_code=201,
)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    return create_patient(db, patient)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db),
):
    patient = get_patient(db, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return patient