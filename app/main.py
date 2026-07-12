from fastapi import FastAPI
from app.routes import doctor # doctor router ko import kar rahy hay

app = FastAPI(title="Hospital Management System")

# Counter ko main gate ke sath connect kar diya
app.include_router(doctor.router)

@app.get("/")
def home():
    return {"message": "Hospital Main Gate Open!"}