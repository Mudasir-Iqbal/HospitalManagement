from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. PostgreSQL ka rasta (URL)
# Format: postgresql://username:password@host:port/database_name
DATABASE_URL = "postgresql://postgres:shikra@localhost:5432/hospital_db"

# 2. Engine banaya (Jo database se physically raabta qaim rakhega)
engine = create_engine(DATABASE_URL)

# 3. SessionFactory (Jab bhi koi user aayega, isko use karke aik naya session/hotline khulegi)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base Class (Is dache ko use karke hum aage chal kar tables banayenge)
Base = declarative_base()