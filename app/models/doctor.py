from sqlalchemy import Column, Integer, String ,Float
from sqlalchemy.orm import relationship
from app.database import Base # Jo Base class database.py mein banayi thi
from app.database import Base

# Humne database table ka structure define kiya
class DoctorModel(Base):
    __tablename__ = "doctors" # Database mein table ka naam ye hoga

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    salary = Column(Float, default=0.0)
# 1. Relationship Line Add Ki (Doctor ke paas multiple patients ho sakte hain)
    patients = relationship("PatientModel", back_populates="doctor", cascade="all, delete-orphan")