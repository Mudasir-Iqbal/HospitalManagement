from fastapi import APIRouter,Depends,HTTPException
from app.schemas.doctor import DoctorCreate # Apne naye form ko import kiya
from sqlalchemy.orm import Session
from app.database import SessionLocal # Hamari session factory
from app.crud.doctor import create_doctor_in_db ,get_all_doctors_from_db, get_doctor_by_id_from_db,update_doctor_in_db, delete_doctor_from_db


router = APIRouter(prefix="/doctor", tags=["Doctors"])
# Helper function jo har request par naya session khola ga aur end mein close karega
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ab ye asli POST handler ban gaya hai
@router.post("/")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    # Humne data aur database session dono CRUD manager ko de diye
    saved_doctor = create_doctor_in_db(db=db, doctor_data=doctor)
    
    return {
        "status": "Success",
        "message": "Doctor MySQL database mein permanently save ho gaya hai!",
        "database_id": saved_doctor.id
    }


# 1. Sab doctors ki list dekhne ka counter
@router.get("/")
def read_all_doctors(db: Session = Depends(get_db)):
    doctors_list = get_all_doctors_from_db(db=db)
    return doctors_list

# 2. Kisi aik doctor ko ID se dhoondne ka counter
@router.get("/{doctor_id}")
def read_doctor_by_id(doctor_id: int, db: Session = Depends(get_db)):
    doctor = get_doctor_by_id_from_db(db=db, doctor_id=doctor_id)
    
    # ⚠️ Master Edge Case Check: Agar database mein wo ID maujood hi na ho?
    if not doctor:
        # Client ko standard 404 error response bhejo
        raise HTTPException(status_code=404, detail="Doctor nahi mila boss!")
        
    return doctor

# 1. Update Counter (PUT Request)
@router.put("/{doctor_id}")
def update_doctor(doctor_id: int, doctor_data: DoctorCreate, db: Session = Depends(get_db)):
    updated_doctor = update_doctor_in_db(db=db, doctor_id=doctor_id, updated_data=doctor_data)
    
    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Update karne ke liye doctor nahi mila!")
        
    return {"message": "Doctor data successfully update ho gaya!", "data": updated_doctor}



# 2. Delete Counter (DELETE Request)
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    success = delete_doctor_from_db(db=db, doctor_id=doctor_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Delete karne ke liye doctor nahi mila!")
        
    return {"message": f"ID {doctor_id} wala doctor database se delete kar diya gaya hai."}


