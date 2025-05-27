from fastapi import FastAPI
from pydantic import  BaseModel

app = FastAPI()

# @app.get("/greet/{name}")
# def greeting_function(name : str):
#     return {"message" : f"Hello, {name}!"}

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message" : f"User {user.name} is {user.age} years old."}