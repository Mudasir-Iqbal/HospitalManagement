from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class PatientModel(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    disease = Column(String(150), nullable=False)
    
    # 🔗 1. Foreign Key: Jo batati hai ke ye column 'doctors' table ki 'id' se juda hai
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="CASCADE"), nullable=False)
    
    # 🕒 2. Admission Date: Jo automatic current time utha legi jab patient admit hoga
    admission_date = Column(DateTime, default=datetime.utcnow)

    # 🔄 3. Relationship (Optional but powerful): Is ki wajah se hum Python mein direct 
    # patient.doctor likh kar uske doctor ka poora data nikal sakte hain bina lambi queries ke!
    doctor = relationship("DoctorModel", back_populates="patients")