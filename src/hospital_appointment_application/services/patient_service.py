from sqlalchemy.orm import Session

from hospital_appointment_application.models.patient import Patient


def get_patients(db: Session):
    return db.query(Patient).all()


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(
        Patient.id == patient_id
    ).first()


def create_patient(db: Session, patient_data):
    patient = Patient(**patient_data.model_dump())

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient