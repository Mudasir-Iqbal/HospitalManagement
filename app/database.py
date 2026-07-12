from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 🟢 MySQL Connection String
# Format: mysql+pymysql://username:password@host:port/database_name
# Username: root, Port: 3306, Password: jo aapka MySQL ka password hai (e.g., shikra)
DATABASE_URL = "mysql+pymysql://root:shikra@localhost:3306/hospital_db"

# 2. Engine banaya (Jo database se physically raabta qaim rakhega)
engine = create_engine(DATABASE_URL)

# 3. SessionFactory (Jab bhi koi user aayega, isko use karke aik naya session/hotline khulegi)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base Class (Is dache ko use karke hum aage chal kar tables banayenge)
Base = declarative_base()