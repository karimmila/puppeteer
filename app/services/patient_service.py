import os
import uuid
from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.crud.patient_crud import create_patient, get_all_patients, get_patient_by_id, get_patient_by_email
from app.schemas.patient import PatientCreate, PatientOut


UPLOAD_DIR = "uploads"

def save_document_photo(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

def get_patient_document_file(db, patient_id: int):
    # Query patient
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Ensure the file exists
    file_path = patient.document_photo
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Get file extension for naming
    extension = file_path[file_path.rfind('.'):]
    return FileResponse(
        file_path,
        media_type="application/octet-stream",
        filename=f"{patient.name}_document{extension}"
    )

def register_patient(db, patient: PatientCreate, document_photo: UploadFile):
    existing_patient = get_patient_by_email(db, patient.email)
    if existing_patient:
        raise HTTPException(status_code=400, detail="Email already registered")
    document_photo_path = save_document_photo(document_photo)
    db_patient = create_patient(db, patient, document_photo_path)
    return db_patient

def get_patients(db):
    patients = get_all_patients(db)
    return patients

def get_patient_document(db, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    return patient
                        
def get_patient(db, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    return patient