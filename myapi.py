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
        "name" : "karl",
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
def get_student(student_id : int = Path(None, description="The ID of the student you want to view" , gt=0 )):
    return students[student_id]