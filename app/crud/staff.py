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
