from pydantic import BaseModel, EmailStr, field_validator
import re

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

    @field_validator("phone")
    def validate_phone(cls, phone):
        phone_pattern = re.compile(r"^\+?[1-9]\d{6,14}$")  
        if not phone_pattern.match(phone):
            raise ValueError("Invalid phone number format. Use E.164 format: 598236236")
        return phone

class PatientOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    document_photo: str

    class Config:
        orm_mode = True

