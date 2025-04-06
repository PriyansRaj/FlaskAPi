from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Serve static folder (for index.html)


app = FastAPI()
class Todo(BaseModel):
    id: int
    title:str
    completed: bool

todo_list: List[Todo] =[]
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")
@app.get("/")
def home():
    return {"message":"Welcome to the Todo "}

@app.get("/todos",response_model=List[Todo])
def get_all_todos():
    return todo_list

@app.post("/todos",response_model=Todo)
def create_todo(todo:Todo):
    todo_list.append(todo)
    return todo

@app.get("/todos/{todo_id}",response_model=Todo)
def get_todo(todo_int:int):
    for todo in todo_list:
        if todo.id == todo_int:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for i,todo in enumerate(todo_list):
        if todo.id ==todo_id:
            del todo_list[i]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")