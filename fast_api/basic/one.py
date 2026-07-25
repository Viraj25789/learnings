from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"greeting":"welcome !"}

@app.get("/about")
def about():
    return{"name":"viraj"}

@app.get("/search")
def student_search(name:str):
    return{"search":name}

@app.get("/student/{id}")
def student_id(id:int):
    return {"student_id":id}



# uvicorn one:app --reload