from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

def create_patient(db: Session, patient: PatientCreate, document_photo_path: str):
    db_patient = Patient(
        name=patient.name,
        email=patient.email,
        phone=patient.phone,
        document_photo=document_photo_path
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_all_patients(db: Session):
    return db.query(Patient).all()

def get_patient_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_patient_by_email(db: Session, email: str):
    return db.query(Patient).filter(Patient.email == email).first()