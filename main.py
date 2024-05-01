import asyncio
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


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
