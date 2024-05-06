from fastapi import FastAPI

from auth import auth_controller
from config.mongodb_provider import example_collection
from users import users_controller

app = FastAPI()
app.include_router(users_controller.router)
app.include_router(auth_controller.router)


@app.get("/")
def root():
    return ""


@app.get("/items/")
async def read_items():
    await example_collection.insert_one({"name": "example"})
    items = await example_collection.find({}).to_list(100)
    return [{"id": str(item["_id"]), "name": item["name"]} for item in items]
