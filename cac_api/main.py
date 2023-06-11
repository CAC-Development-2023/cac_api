from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {
        "Hello": "world"
    }


@app.get("/item/{item-id}")
def read_item(item_id: int, quantity: Union[str, None] = None):
    return {
        "item_id": item_id,
        "quantity": quantity
    }
