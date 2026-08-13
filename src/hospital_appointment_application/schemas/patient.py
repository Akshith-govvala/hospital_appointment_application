from pydantic import BaseModel, EmailStr


class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class PatientResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True