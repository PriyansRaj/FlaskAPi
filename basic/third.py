from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
@app.get("/cube/{number}")
def cube(number:int):
    return {"number": number,"cube":number**3}