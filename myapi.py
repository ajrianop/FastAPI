# Builnding our first API
from fastapi import FastAPI

# We create an instance of the API object
app = FastAPI()

# We create and endopoint (URL)

@app.get("/")

def index():
    '''

    The return is a normal JSON
    '''
    return {"name": "First Data"}