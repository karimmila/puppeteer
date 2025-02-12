from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.patient import PatientCreate, PatientOut
from app.services.patient_service import register_patient, get_patients, get_patient, get_patient_document_file
from app.services.notification_service import send_confirmation_email, send_confirmation_sms
from app.config import settings

router = APIRouter()

# Future-proof by checking environment feature flag to enable/disable SMS Notification
ENABLE_SMS = settings.ENABLE_SMS

@router.post("/patients/", response_model=PatientOut)
async def create_patient(
    background_tasks: BackgroundTasks,
    name: str,
    email: str,
    phone: str,
    document_photo: UploadFile,
    db: Session = Depends(get_db)
):
    # Validate incoming data via Pydantic
    try:
        patient_data = PatientCreate(name=name, email=email, phone=phone)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Create the patient record (file is saved and DB record inserted)
    db_patient = register_patient(db, patient_data, document_photo)
    
    # Asynchronously send a confirmation email to avoid blocking
    background_tasks.add_task(send_confirmation_email, db_patient.email, db_patient.name)

    # 🔹 Prepare for SMS feature but keep it disabled until ready
    if ENABLE_SMS:
        message = "Welcome to the platform!"
        background_tasks.add_task(send_confirmation_sms, db_patient.phone, db_patient.name, message)
    
    return db_patient

@router.get("/patients/", response_model=list[PatientOut])
async def get_patients_list(db: Session = Depends(get_db)):
    return get_patients(db)

@router.get("/patients/{patient_id}", response_model=PatientOut)
async def get_patient_document(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
    
@router.get("/patients/{patient_id}/document", response_class=FileResponse)
def download_patient_photo(patient_id: int, db: Session = Depends(get_db)):
    return get_patient_document_file(db, patient_id)
