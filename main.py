from typing import Union 
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello " : "World"}

@app.get("/items/{items_id}")
def read_item(item_id : int , q: Union[str,None] = None):
    return {"item:id":item_id,"q":q}