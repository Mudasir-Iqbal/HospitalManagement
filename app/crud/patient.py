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


