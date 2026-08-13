from sqlalchemy.orm import Session

from hospital_appointment_application.models.doctor import Doctor


def get_doctors(db: Session):
    return db.query(Doctor).all()


def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()


def create_doctor(db: Session, doctor_data):
    doctor = Doctor(**doctor_data.model_dump())

    db.add(doctor)
    db.commit()
    db.refresh(doctor)

    return doctor