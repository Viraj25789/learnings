import sqlite3

try:
    conn = sqlite3.connect("user.db",check_same_thread=False)
    cursor = conn.cursor()
    print("db created.")
except Exception as e:
    print("error in db create",e)


try:
    cursor.execute("""  CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TXT,
            email TEXT UNIQUE,
            password TEXT)
            """)
    conn.commit()
    print("table succesfull")
except Exception as e:
    print("table not created",e)

