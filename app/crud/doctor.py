from sqlalchemy.orm import Session
from app.models.doctor import DoctorModel
from app.schemas.doctor import DoctorCreate

def create_doctor_in_db(db: Session, doctor_data: DoctorCreate):
    # 1. Pydantic ka data utha kar SQL Table ke model mein fit kiya
    new_doctor = DoctorModel(
        name=doctor_data.name,
        specialization=doctor_data.specialization,
        email=doctor_data.email
    )
    
    db.add(new_doctor)       # 2. Database queue mein add kiya
    db.commit()             # 3. Asli hard drive par save (Commit) kiya!
    db.refresh(new_doctor)  # 4. ID automatic generate ho kar object mein load ho jayegi
    
    return new_doctor