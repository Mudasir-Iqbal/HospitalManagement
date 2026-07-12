from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.patient import PatientCreate
from app.crud.patient import create_patient_in_db,get_all_patients_from_db, get_patients_by_doctor_from_db, delete_patient_from_db
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

# 🟢 1. Saare patients dekhne ka counter
@router.get("/")
def read_all_patients(db: Session = Depends(get_db)):
    return get_all_patients_from_db(db=db)

# 🟢 2. Kisi specific Doctor ke patients filter karne ka counter
@router.get("/by-doctor/{doctor_id}")
def read_patients_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    patients = get_patients_by_doctor_from_db(db=db, doctor_id=doctor_id)
    return patients

# 🟢 3. Patient ko discharge/delete karne ka counter
@router.delete("/{patient_id}")
def discharge_patient(patient_id: int, db: Session = Depends(get_db)):
    success = delete_patient_from_db(db=db, patient_id=patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient nahi mila!")
    return {"message": f"Patient ID {patient_id} successfully discharge/delete ho gaya hai."}