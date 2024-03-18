# Builnding our first API
from fastapi import FastAPI, Path

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
    }
}

# We create and endopoint (URL)
@app.get("/")
def index():
    '''
    The return is a normal JSON
    '''
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description="input the Id of the student", gt=0, lt=3 )):

    return students[student_id]