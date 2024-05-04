from fastapi import APIRouter, Depends

from config.database import Session, get_db
from users import users_service

router = APIRouter()


@router.get("/users", tags=["users"])
async def read_users(session: Session = Depends(get_db)):
    return users_service.get_users(session)


@router.get("/users/{user_id}", tags=["users"])
async def get_one_user_by_id(user_id: int, session: Session = Depends(get_db)):
    return users_service.get_one_user_by_id(session, user_id)
