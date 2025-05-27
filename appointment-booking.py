from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

appointments = []

class User(BaseModel):
    patient_name: str
    doctor_name: str
    appointment_date: datetime
    

@app.post("/appointments")
def create_appointment(user: User):
    appointment_id = len(appointments) + 1
    appointment = {
        "id": appointment_id,
        "patient_name": user.patient_name,
        "doctor_name": user.doctor_name,
        "appointment_date": user.appointment_date
    }
    appointments.append(appointment)
    return{"message" : f"Appointment has been succesfully booked for {user.patient_name} with {user.doctor_name} on {user.appointment_date}",
           "appointment_id" : appointment_id}


@app.get("/appointments")
def view_appointments():
    return appointments    
