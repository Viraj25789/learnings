import sqlite3

try:
    conn = sqlite3.connect(database="database.db")
    cursor = conn.cursor()
    print("Database connected..")
except:
    print("Error in connection!")

def creat_table():
        try:
            cursor.execute(f""" 
                   CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   marks INTEGER
                   )
            """)
            conn.commit()
            print("creat table succesfully..")

        except Exception as e:
            print("Error in creat table!",e)


def insert_student():
        try:
            name= input("name: ")
            age= int(input("age: "))
            marks= int(input("marks: "))
        
            cursor.execute(""" 
                           INSERT INTO students (name,age,marks) 
                           VALUES (?,?,?)
                           """,(name,age,marks)
            )
            conn.commit()
            print("insert student succesfully..")

        except Exception as e:
            print("Error in inserting!",e)

def update_student():
        try:
            age= int(input("age: "))
            marks= int(input("marks: "))
            id = int(input("id: "))

            cursor.execute(""" 
                           UPDATE students
                           SET age=?, marks=?
                           Where id=?
                           """,(age,marks,id)
            )
            conn.commit()
            print("update student succesfully..")

        except Exception as e:
            print("Error in updating!",e)

def delete_student():
        try:
            name= input("name: ")
            cursor.execute(""" 
                           DELETE FROM students
                           Where name=?
                           """,(name,)
            )
            conn.commit()
            print("delete student succesfully..")

        except Exception as e:
            print("Error in deleting!",e)

def all_students():
        try:
            cursor.execute(""" 
                           SELECT * FROM students
                           """
            )

            data = cursor.fetchall()
            # data = cursor.fetchone()  gives 1 student only

            for i in data:
                 print(i)

            print("fetch all students succesfully..")

        except Exception as e:
            print("Error in display!",e)


def search_student():
    
        name = input("Enter name: ")
        cursor.execute(
            """
            SELECT *
            FROM students
            WHERE name = ?
            """,
            (name,)
        )
        data = cursor.fetchall()
        for student in data:
            print(student)
        
