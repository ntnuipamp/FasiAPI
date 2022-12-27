from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}  # Declare an empty dictionary to store the items

class Item(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    items[item.id] = item  # Store the item in the dictionary
    return {"id": item.id}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id)  # Return the item with the specified id

# uvicorn app2:app --reload