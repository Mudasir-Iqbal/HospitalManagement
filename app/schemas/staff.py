from pydantic import BaseModel

# Input form jab naya staff member register hoga [cite: 150, 153]
class StaffCreate(BaseModel):
    name: str
    role: str
    shift: str
    salary: float