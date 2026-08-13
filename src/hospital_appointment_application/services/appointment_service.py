from fastapi import HTTPException
from sqlalchemy.orm import Session

from hospital_appointment_application.models.appointment import Appointment
from hospital_appointment_application.models.doctor import Doctor
from hospital_appointment_application.models.patient import Patient


def get_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment(db: Session, appointment_id: int):
    return (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )


def create_appointment(db: Session, appointment_data):

    # Validate time range
    if appointment_data.appointment_start >= appointment_data.appointment_end:
        raise HTTPException(
            status_code=400,
            detail="Appointment end time must be after start time",
        )

    # Check patient exists
    patient = (
        db.query(Patient)
        .filter(Patient.id == appointment_data.patient_id)
        .first()
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    # Check doctor exists
    doctor = (
        db.query(Doctor)
        .filter(Doctor.id == appointment_data.doctor_id)
        .first()
    )

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found",
        )

    # Check overlapping appointments
    overlap = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == appointment_data.doctor_id,
            Appointment.appointment_start
            < appointment_data.appointment_end,
            Appointment.appointment_end
            > appointment_data.appointment_start,
        )
        .first()
    )

    if overlap:
        raise HTTPException(
            status_code=400,
            detail="Appointment overlaps with existing appointment",
        )

    appointment = Appointment(
        patient_id=appointment_data.patient_id,
        doctor_id=appointment_data.doctor_id,
        appointment_start=appointment_data.appointment_start,
        appointment_end=appointment_data.appointment_end,
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment