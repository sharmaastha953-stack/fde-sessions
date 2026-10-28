from fastapi import FastAPI, HTTPException

app = FastAPI(title="Example REST API", description="Example endpoints for learning FastAPI")

items = {
    1: {"id": 1, "name": "Laptop", "price": 999.99},
    2: {"id": 2, "name": "Mouse", "price": 29.99},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Example REST API"}


@app.get("/items")
def get_items():
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(item: dict):
    item_id = max(items, default=0) + 1
    new_item = {"id": item_id, **item}
    items[item_id] = new_item
    return new_item
