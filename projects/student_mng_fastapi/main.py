from fastapi import FastAPI
from database import conn, cursor
from fast_api.student_mng.models import Students

app = FastAPI()


@app.post("/student")
def add_student(student=Students):
    cursor.execute("""
            INSERT INTO students(
            name,age,marks) 
            VALUES(?,?,?)""",
            (student.name,student.age,student.marks))
    conn.commit()
    return """{
    "id":student.id
    "name":student.name,
    "age": student.age,
    "marks":student.marks}"""

@app.get("/students")
def get_students():
    cursor.execute(
        "SELECT * FROM students"
    )
    data = cursor.fetchall()
    return data