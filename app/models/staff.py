from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class StaffModel(Base):
    __tablename__ = "staff" # Table ka naam database mein 'staff' hoga [cite: 145]

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)   # e.g., Nurse, Receptionist, Lab Tech [cite: 186]
    shift = Column(String(20), nullable=False)  # e.g., Morning, Night, Evening
    salary = Column(Float, nullable=False)