from sqlalchemy import Column, Integer, String
from app.database import Base # Jo Base class database.py mein banayi thi

# Humne database table ka structure define kiya
class DoctorModel(Base):
    __tablename__ = "doctors" # Database mein table ka naam ye hoga

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)