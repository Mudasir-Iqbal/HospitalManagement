from fastapi import APIRouter
from app.schemas.doctor import DoctorCreate # Apne naye form ko import kiya

router = APIRouter(prefix="/doctor", tags=["Doctors"])

# 🟢 Naya POST counter banaya data submit karne ke liye
@router.post("/")
def create_doctor_temporary(doctor: DoctorCreate):
    # Abhi hamare paas database nahi hai, to hum sirf check karne ke liye 
    # client ka bheja hua data wapas response mein dikha rahe hain
    return {
        "status": "Success (Temporary)",
        "message": "Data router tak sahi pohnch gaya aur validation pass ho gayi!",
        "data": doctor
    }

@router.get("/")
def check_doctor_counter():
    return {"message": "Doctor counter active hai!"}