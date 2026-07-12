from fastapi import APIRouter

# now create doctor counter manager
router = APIRouter(prefix="/doctor", tags=["Doctors"])

@router.get("/")
def check_doctor_counter():
    return {"message": "Doctor counter active hai, lekin abhi koi database connect nahi hai!"}