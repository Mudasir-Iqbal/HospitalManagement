from fastapi import APIRouter,Depends
from app.schemas.doctor import DoctorCreate # Apne naye form ko import kiya
from sqlalchemy.orm import Session
from app.database import SessionLocal # Hamari session factory
from app.crud.doctor import create_doctor_in_db # CRUD function import kiya


router = APIRouter(prefix="/doctor", tags=["Doctors"])
# Helper function jo har request par naya session khola ga aur end mein close karega
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🟢 Ab ye asli POST handler ban gaya hai
@router.post("/")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    # Humne data aur database session dono CRUD manager ko de diye
    saved_doctor = create_doctor_in_db(db=db, doctor_data=doctor)
    
    return {
        "status": "Success",
        "message": "Doctor MySQL database mein permanently save ho gaya hai!",
        "database_id": saved_doctor.id
    }

