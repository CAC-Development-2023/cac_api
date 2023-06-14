# Author(s): [Sable <sable262021[at]gmail[dot]com>]
# Last Modified: 14/6/2023

from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/")
def get_root():
    return StaticFiles(directory="../cac_vue_frontend/dist", html=True)

<<<<<<< HEAD
@app.get("/item/{item-id}")
def read_item(item_id: int, quantity: Union[str, None] = None):
    return {
        "item_id": item_id,
        "quantity": quantity
    }
=======
# 14/6/2023 Sable <sable262021[at]gmail[dot]com>
# TODO: read song name from JSON file
@app.get("/api/v1/get_song_names", response_class=ORJSONResponse)
def get_song_names():
    return {
        "song_names":"TODO"
    }
>>>>>>> 1978bf8 (Added author annotations + gitmodule)
