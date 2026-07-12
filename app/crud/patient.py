from sqlalchemy.orm import Session
from app.models.patient import PatientModel
from app.schemas.patient import PatientCreate

def create_patient_in_db(db: Session, patient_data: PatientCreate):
    # 1. Pydantic form ka data utha kar SQL table model mein convert kiya
    new_patient = PatientModel(
        name=patient_data.name,
        age=patient_data.age,
        gender=patient_data.gender,
        disease=patient_data.disease,
        doctor_id=patient_data.doctor_id
    )
    
    db.add(new_patient)       # 2. Database queue mein add kiya
    db.commit()             # 3. Hard drive par permanently save kiya
    db.refresh(new_patient)  # 4. ID aur admission_date automatic sync ho jayengi
    
    return new_patient

# 1. Saare patients read karne ka function
def get_all_patients_from_db(db: Session):
    return db.query(PatientModel).all()

# 2. Kisi specific doctor ke saare patients dhoondne ka function (Advanced Analysis)
def get_patients_by_doctor_from_db(db: Session, doctor_id: int):
    return db.query(PatientModel).filter(PatientModel.doctor_id == doctor_id).all()

# 3. Patient delete karne ka function
def delete_patient_from_db(db: Session, patient_id: int):
    db_patient = db.query(PatientModel).filter(PatientModel.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return True
    return False
