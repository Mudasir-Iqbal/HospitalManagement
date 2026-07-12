from sqlalchemy.orm import Session
from app.models.doctor import DoctorModel
from app.schemas.doctor import DoctorCreate

def create_doctor_in_db(db: Session, doctor_data: DoctorCreate):
    # 1. Pydantic ka data utha kar SQL Table ke model mein fit kiya
    new_doctor = DoctorModel(
        name=doctor_data.name,
        specialization=doctor_data.specialization,
        email=doctor_data.email
        phone=doctor_data.phone,     
        salary=doctor_data.salary
    )
    
    db.add(new_doctor)       # 2. Database queue mein add kiya
    db.commit()             # 3. Asli hard drive par save (Commit) kiya!
    db.refresh(new_doctor)  # 4. ID automatic generate ho kar object mein load ho jayegi
    
    return new_doctor


# 1. Pura data read karne ka function
def get_all_doctors_from_db(db: Session):
    # SQL equivalent: SELECT * FROM doctors;
    return db.query(DoctorModel).all()

# 2. Specific ID se data read karne ka function
def get_doctor_by_id_from_db(db: Session, doctor_id: int):
    # SQL equivalent: SELECT * FROM doctors WHERE id = doctor_id LIMIT 1;
    return db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()


# 1. Update Karne Ka Function
def update_doctor_in_db(db: Session, doctor_id: int, updated_data: DoctorCreate):
    # Pehle us doctor ko dhoondho jise badalna hai
    db_doctor = db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()
    
    if db_doctor:
        # Purane data ki jagah naya data set karo
        db_doctor.name = updated_data.name
        db_doctor.specialization = updated_data.specialization
        db_doctor.email = updated_data.email
        
        db.commit()        # Changes ko save kiya
        db.refresh(db_doctor) # Object ko sync kiya
    return db_doctor


# 2. Delete Karne Ka Function
def delete_doctor_from_db(db: Session, doctor_id: int):
    db_doctor = db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()
    
    if db_doctor:
        db.delete(db_doctor) # Database state se delete kiya
        db.commit()          # Permanent delete confirm kiya
        return True
    return False