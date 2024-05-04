from fastapi import FastAPI

from users import users_controller

app = FastAPI()
app.include_router(users_controller.router)


@app.get("/")
def root():
    return ""
