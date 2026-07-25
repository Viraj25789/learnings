from student_manage import *
import json

# try:
#     with open("student.json", "r") as file:
#         students = json.load(file)

# except FileNotFoundError:
#     students = []


def add_student():

    name= input("name: ")
    age= int(input("age"))
    marks= int(input("marks"))

    insert_student(name,age,marks)
   

def view_all_students():
    all_students()


def search_student():
    search_student_db()

def maximum_marks():

    try:
        cursor.execute(""" 
                    SELECT * FROM students
                    """
        )
        data = cursor.fetchall()

        max=[]
        for student in data:
            max.append(student[3])
            max.sort()
            max.reverse()
        print(f"maximum marks is {max[0]}")
    except Exception as e:
        print("Error to find maximum marks!",e)
        
def delete_student():
    delete_student_db()

def update_marks():
    update_student()

def statics():
    statics_student()
    

   
