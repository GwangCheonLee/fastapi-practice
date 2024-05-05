from fastapi import FastAPI

from auth import auth_controller
from users import users_controller

app = FastAPI()
app.include_router(users_controller.router)
app.include_router(auth_controller.router)


@app.get("/")
def root():
    return ""
