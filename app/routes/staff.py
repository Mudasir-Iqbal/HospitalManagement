from fastapi import APIRouter,Depends,HTTPException
from app.schemas.staff import StaffCreate # Apne naye form ko import kiya
from sqlalchemy.orm import Session
from app.database import SessionLocal # Hamari session factory
from app.crud.staff import create_staff_in_db ,get_all_staff_from_db, get_staff_by_id_from_db,update_staff_in_db,delete_staff_from_db


router = APIRouter(prefix="/staff", tags=["Staff"])
# Helper function jo har request par naya session khola ga aur end mein close karega
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ab ye asli POST handler ban gaya hai
@router.post("/")
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    # Humne data aur database session dono CRUD manager ko de diye
    saved_staff = create_staff_in_db(db=db, staff_data=staff)
    
    return {
        "status": "Success",
        "message": "staff MySQL database mein permanently save ho gaya hai!",
        "database_id": saved_staff.id
    }


# 1. Sab staff ki list dekhne ka counter
@router.get("/")
def read_all_staff(db: Session = Depends(get_db)):
    staff_list = get_all_staff_from_db(db=db)
    return staff_list

# 2. Kisi aik staff ko ID se dhoondne ka counter
@router.get("/{staff_id}")
def read_staff_by_id(staff_id: int, db: Session = Depends(get_db)):
    staff = get_staff_by_id_from_db(db=db, staff_id=staff_id)
    
    # Master Edge Case Check: Agar database mein wo ID maujood hi na ho?
    if not staff:
        # Client ko standard 404 error response bhejo
        raise HTTPException(status_code=404, detail="staff nahi mila boss!")
        
    return staff

# 1. Update Counter (PUT Request)
@router.put("/{staff_id}")
def update_staff(staff_id: int, staff_data: StaffCreate, db: Session = Depends(get_db)):
    updated_staff = update_staff_in_db(db=db, staff_id=staff_id, updated_data=staff_data)
    
    if not updated_staff:
        raise HTTPException(status_code=404, detail="Update karne ke liye staff nahi mila!")
        
    return {"message": "staff data successfully update ho gaya!", "data": updated_staff}



# 2. Delete Counter (DELETE Request)
@router.delete("/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    success = delete_staff_from_db(db=db, staff_id=staff_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Delete karne ke liye staff nahi mila!")
        
    return {"message": f"ID {staff_id} wala staff database se delete kar diya gaya hai."}


