import sqlite3

# connection db
try:
    conn = sqlite3.connect(database="student_management.db")
    cursor = conn.cursor()
    print("database connected..")
except Exception as e:
    print("database connection error!",e)

# table create
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    marks INTEGER
    )""")
    conn.commit()
    print("table created succesfully...")
except Exception as e:
    print("error in create table!",e)
    

def insert_student(name,age,marks):
        try:
            cursor.execute(""" 
                           INSERT INTO students (name,age,marks) 
                           VALUES (?,?,?)
                           """,(name,age,marks)
            )
            conn.commit()
            print("insert student succesfully..")

        except Exception as e:
            print("Error in inserting!",e)


def all_students():
        try:
            cursor.execute(""" 
                           SELECT * FROM students
                           """
            )

            data = cursor.fetchall()
            # data = cursor.fetchone()  gives 1 student only

            for i in data:
                 print(f""" Name: {i[1]} age: {i[2]} marks: {i[3]}""")

            print("fetch all students succesfully..")

        except Exception as e:
            print("Error in display!",e)

def search_student_db():
    
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
        if data==[]:
             print("No student founded!")
        else:
            print("Student founded..")
            for i in data:
                print(f"""Name: {i[1]} age: {i[2]} marks: {i[3]}""")

def update_student():
        try:
            name = input("new name: ")
            age= int(input("new age: "))
            marks= int(input("new marks: "))
            id = int(input("id: "))

            cursor.execute(""" 
                           UPDATE students
                           SET name=?, age=?, marks=?
                           Where id=?
                           """,(name,age,marks,id)
            )
            conn.commit()
            print("update student succesfully..")

        except Exception as e:
            print("Error in updating!",e)

def delete_student_db():
        try:
            id= input("id: ")
            cursor.execute(""" 
                           DELETE FROM students
                           Where id=?
                           """,(id,)
            )
            conn.commit()
            print("delete student succesfully..")

        except Exception as e:
            print("Error in deleting!",e)


def statics_student():
    try:
        cursor.execute(""" 
                SELECT * FROM students
                """
        )
        data = cursor.fetchall()
        print(f"total students: ",len(data))
    except Exception as e:
            print("total not founded!",e)

    try:
        total_marks= [i[3] for i in data]
        avg = sum(total_marks)/len(data)
        print(f"avarage marks: ",avg)
    except Exception as e:
        print("avg not founded!",e)

    try:
        count= total_marks[0]
        for i in total_marks:
            if i>count:
                count=i
        print(f"highest marks: ",count)

        count_negative=count
        for i in total_marks:
                if i<count_negative:
                    count_negative=i
        print(f"lowest marks: ",count_negative)
    except Exception as e:
            print("maximum and minimum not founded!",e)

    try:
        passed= [i[3] for i in data if i[3]>=35]
        failed= [i[3] for i in data if i[3]<35]

        print(f"total passed students are: {len(passed)}")
        print(f"total failed students are: {len(failed)}")
    except Exception as e:
            print("passed and failed students are not founded!",e)



