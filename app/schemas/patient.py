from pydantic import BaseModel

# Naye Patient ka input form (Validation Layer)
class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    disease: str
    doctor_id: int  # Yeh lazmi hoga taake pata chale mareez kis doctor ka hai