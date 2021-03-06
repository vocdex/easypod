"""FastAPI is a blazing fast, simple, and flexible API Framework for Python."""


from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}
@app.get("/users/me")
async def read_user_me():
    return {"user": "the current user"}
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name==ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name==ModelName.lenet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    if model_name==ModelName.resnet:
        return {"model_name": model_name, "message": "Just a plain Resnet-101"}
    return {"model_name": model_name, "message": "Unknown model name"}