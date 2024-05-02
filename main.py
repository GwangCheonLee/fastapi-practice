import asyncio
from enum import Enum
from typing import List, Annotated

from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str

    class Config:
        extra = "forbid"


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


async def mok_db_query():
    await asyncio.sleep(5)
    return [{"name": "Item1"}, {"name": "Item2"}]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/", response_model=List[Item])
async def read_items():
    items = await mok_db_query()
    return items


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/inject")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/practice/query")
def query(q: str = None):
    return q


@app.post("/items/")
async def create_item(item: Item):
    return item.dict()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


async def verify_token(x_token: Annotated[str, Header()]):
    print(x_token)
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    print(x_key)
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/dependency", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
