from sqlalchemy.orm import Session
from app.models.staff import StaffModel
from app.schemas.staff import StaffCreate


def create_staff_in_db(db: Session, staff_data: StaffCreate):
    # 1. Pydantic ka data utha kar SQL Table ke model mein fit kiya
    new_staff = StaffModel(
        name=staff_data.name,
        role=staff_data.role,
        shift=staff_data.shift,  
        salary=staff_data.salary
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff




# 1. Pura data read karne ka function
def get_all_staff_from_db(db: Session):
    # SQL equivalent: SELECT * FROM staff;
    return db.query(StaffModel).all()

# 2. Specific ID se data read karne ka function
def get_staff_by_id_from_db(db: Session, staff_id: int):
    # SQL equivalent: SELECT * FROM staff WHERE id = staff_id LIMIT 1;
    return db.query(StaffModel).filter(StaffModel.id == staff_id).first()


# 1. Update Karne Ka Function
def update_staff_in_db(db: Session, staff_id: int, updated_data: StaffCreate):
    # Pehle us staff ko dhoondho jise badalna hai
    db_staff = db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    
    if db_staff:
        # Purane data ki jagah naya data set karo
        db_staff.name = updated_data.name
        db_staff.role = updated_data.role
        db_staff.shift = updated_data.shift
        db_staff.salary = updated_data.salary
        
        db.commit()        # Changes ko save kiya
        db.refresh(db_staff) # Object ko sync kiya
    return db_staff


# 2. Delete Karne Ka Function
def delete_staff_from_db(db: Session, staff_id: int):
    db_staff = db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    
    if db_staff:
        db.delete(db_staff) # Database state se delete kiya
        db.commit()          # Permanent delete confirm kiya
        return True
    return False