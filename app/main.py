from fastapi import FastAPI
from app.routes import doctor,patient # doctor router ko import kar rahy hay
from app.database import engine, Base
from app.models import doctor as doctor_model # Model ko import karna zaroori hai taake Base ko pata chale
from app.models import patient as patient_model


# Ye line server start hote hi models ko check karegi aur PostgreSQL mein tables bana degi!
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System")

# Counter ko main gate ke sath connect kar diya
app.include_router(doctor.router)
app.include_router(patient.router)

@app.get("/")
def home():
    return {"message": "Hospital Main Gate Open!"}