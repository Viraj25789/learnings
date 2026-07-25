from models import Student
import json

try:
    with open("student.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []


def add_student():

    name= input("name: ")
    age= int(input("age"))
    marks= int(input("marks"))

    student = Student(name,age,marks)
    student_to_dict = student.to_dict()
    students.append(student_to_dict)

    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)


def view_all_students():

    with open("student.json","r") as file:
        data = json.load(file)

    for student in data:
        print(f"names:{student["name"]} age: {student["age"]} marks: {student["marks"]}")

def search_student():

    search = input("Enter name of student: ")
    search = search.lower()

    with open("student.json","r") as file:
        data = json.load(file)

    for student in data:
        if student["name"]==search:
            print(f"Student founded \nnames:{student["name"]} age: {student["age"]} marks: {student["marks"]}")

def maximum_marks():

    with open("student.json","r") as file:
        data = json.load(file)
    max=[]
    for student in data:
        max.append(student["marks"])
        max.sort()
        max.reverse()
    print(f"maximum marks by student is {max[0]}")
        
def delete_student():

    name = input("Enter student name: ")
    with open("student.json","r") as file:
        data = json.load(file)

    found = False

    for student in data:
        if student["name"].lower() == name.lower():
            data.remove(student)
            found = True
            break
    if found:
        with open("student.json","w") as file:
            json.dump(data,file,indent=4)
        print("Student deleted.")
    else:
        print("Student not found.")

def update_marks():

    name = input("Enter student name: ")
    new_marks = int(input("New marks: "))

    with open("student.json","r") as file:
        data = json.load(file)

    found = False

    for student in data:

        if student["name"].lower() == name.lower():

            student["marks"] = new_marks
            found = True
            break

    if found:

        with open("student.json","w") as file:
            json.dump(data,file,indent=4)

        print("Marks updated.")

    else:
        print("Student not found.")

def statics():

    print("total students are: ",len(students))

    marks = [student["marks"] for student in students]
    avg = sum(marks)/len(marks)
    print(f"avarage marks: ",avg)

    count=0
    for i in marks:
        if i>count:
            count=i
    print(f"highest marks: ",count)


    for i in marks:
        if i<count:
            count=i
    print(f"lowest marks: ",count)

    passed = [student for student in students if student["marks"]>=35]

    print(f"passed studens: ", len(passed))

    failed = [student for student in students if student["marks"]<35]

    print(f"failed studens: ", len(failed))
    
    