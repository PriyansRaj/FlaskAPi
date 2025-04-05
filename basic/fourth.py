from fastapi import FastAPI

app = FastAPI()
@app.get("/greet")
def greet(name: str = "friend"):
    return {"message": f"Hello, {name}!"}