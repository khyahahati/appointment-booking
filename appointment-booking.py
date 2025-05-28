from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

appointments = []

class User(BaseModel):
    patient_name: str
    doctor_name: str
    appointment_date: datetime
    
#Create an appointment 
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

#View an appointment
@app.get("/appointments")
def view_appointments():
    return appointments    

#Cancel an appointment
@app.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: int):
    for i, appt in enumerate(appointments):
        if appt["id"] == appointment_id:
            cancelled_appointment = appointments.pop(i)
            return {
                "message" : f"The appointment for {cancelled_appointment['patient_name']} with {cancelled_appointment['doctor_name']} on {cancelled_appointment['appointment_date']} has been cancelled."
            }
    raise HTTPException(status_code=404, detail= "Appointment not found")
        
    