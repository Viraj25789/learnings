from pydantic import BaseModel

class Students(BaseModel):
    name:str
    age:int
    marks:int

