from pydantic import BaseModel

# Humne aik blueprint (schema) banaya naye doctor ke form ke liye
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: str
    phone: str
    salary: float