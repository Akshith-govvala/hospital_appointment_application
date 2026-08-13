from pydantic import BaseModel


class DoctorCreate(BaseModel):
    name: str
    specialization: str


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str

    class Config:
        from_attributes = True