from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    marks: int

@app.post("/students")
def add_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "marks": student.marks
    }




class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    marks: int

@app.get("/student", response_model=StudentResponse)
def get_student():
    return {
        "id": 1,
        "name": "Viraj",
        "age": 22,
        "marks": 90,
        "password": "123456"
    }
# no passwd in response.