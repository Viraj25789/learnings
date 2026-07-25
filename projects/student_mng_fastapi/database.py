import sqlite3

conn = sqlite3.connect("student_mng_api.db")
cursor = conn.cursor()
print("Connection succesfull..")


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
marks INTEGER)""")
conn.commit()
print("Table created succesfully..")



    
