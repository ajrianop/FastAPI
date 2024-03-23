# Builnding our first API
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# We create an instance of the API object
app = FastAPI()

students = {
    1 : {
        "name" : "karl",
        "age" : "11",
        "class" : "year 6"
    },
    2 : {
        "name" : "paul",
        "age" : "12",
        "class" : "year 7"
    },
    3 : {
        "name" : "brick",
        "age" : "11",
        "class" : "year 6"
    },
    4 : {
        "name" : "jane",
        "age" : "10",
        "class" : "year 5"
    },
    5 : {
        "name" : "gibi",
        "age" : "9",
        "class" : "year 4"
    }
}

# Creating a new class

class Student(BaseModel):
    name: str
    age: int
    year: str


# We create and endopoint (URL)
@app.get("/")
def index():
    '''
    The return is a normal JSON
    '''
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description="The Id of the student", gt=0, lt=7 )):

    return students[student_id]

# Query parameters

@app.get("/get-by-name")

def get_student(name : Optional[str] = None , test = int):

    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data' : 'Not found'}

# Combining path and query parameters

@app.get("/get-by-name/{student_id}")

def get_student(student_id : int , name : Optional[str] = None , test = int):
    if student_id == None:
        for student_id in students:
            if students[student_id]['name'] == name:
                return students[student_id]
        return {'Data' : 'Not found'}
    else:
        return students[student_id]

# Request body and the post method
# With the following command we can save the data of a new student
@app.post("/create-student/{student-id}")
def create_student(student_id : int , student : Student):
    if student_id in students:
        return {"Error": "the student already exist"}

    students[student_id] = student
    return students[student_id]

