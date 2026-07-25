from fastapi import FastAPI, Depends
from fast_api.auth.schema import UserRegister,UserLogin
from fast_api.auth.security import *
from database import *
from fast_api.auth.token_handler import *

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Authentication API"
    } 

@app.post("/register")
def register(user: UserRegister):

    try:
        hashed = hash_password(user.password)
        print("hash generated")

        cursor.execute("""
            INSERT INTO users(name,email,password)
            VALUES(?,?,?)""",
            (user.name,user.email,hashed)
            )
        conn.commit()
        print("insert succesfully.")
    except Exception as e:
        print("not inserted",e)

    return {
        "message":"User registered."
                }

@app.post("/login")
def login(user: UserLogin):

    cursor.execute(
    """
    SELECT * FROM users
    WHERE email = ?
    """,
    (user.email,)
    )

    db_user = cursor.fetchone()

    if db_user is None:
        return {
            "message":"User not found"
        }
    if not verify_password(
        user.password,
        db_user[3]
    ):
        return {
            "message": "Invalid Password"
        }
    token = create_access_token(
        {
            "user_id": db_user[0],
            
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/profile")
def profile(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_token(token)

    user_id = payload["user_id"]

    cursor.execute(
        """
        SELECT name,email
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    return {
        "id": user_id,
        "name": user[0],
        "email": user[1]
    }