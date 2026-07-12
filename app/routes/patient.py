from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.patient import PatientCreate
from app.crud.patient import create_patient_in_db
from app.models.doctor import DoctorModel # Doctor verify karne ke liye import kiya

router = APIRouter(prefix="/patient", tags=["Patients"])

# Database session dependency helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def admit_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    # ⚠️ Master Edge Case Check: Kya jo doctor_id bheji hai, wo asliyat mein exist karti hai?
    doctor_exists = db.query(DoctorModel).filter(DoctorModel.id == patient.doctor_id).first()
    
    if not doctor_exists:
        # Agar doctor nahi mila, to patient admit nahi ho sakta!
        raise HTTPException(status_code=400, detail="Bhai, ye Doctor ID database mein mojood hi nahi hai!")
        
    # Agar doctor mojood hai, to CRUD manager ko bolo save karey
    saved_patient = create_patient_in_db(db=db, patient_data=patient)
    
    return {
        "status": "Success",
        "message": "Patient successfully admit ho gaya hai!",
        "patient_id": saved_patient.id,
        "admitted_to_doctor_id": saved_patient.doctor_id
    }