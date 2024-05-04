from fastapi import APIRouter, Depends

from config.database import Session, get_db

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(session: Session = Depends(get_db)):
    session
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
