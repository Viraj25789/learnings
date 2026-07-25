from fastapi import FastAPI

app = FastAPI()

students = []


@app.get("/students")
def get_students():

    return students


@app.post("/students")
def add_student(name: str):

    students.append(name)

    return {
        "message": "Student Added",
        "students": students
    }


@app.put("/students/{id}")
def update_student(id: int, name: str):

    students[id] = name

    return students


@app.delete("/students/{id}")
def delete_student(id: int):

    deleted = students.pop(id)

    return {
        "deleted": deleted,
        "students": students
    }