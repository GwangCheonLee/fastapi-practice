from typing import Union

from fastapi import APIRouter, Depends

from config.database import Session, get_db
from filters.jwt_filter import jwt_filter
from schema import User
from users import users_service
from users.dto.user_dto import UserDto, CreateUserDto

router = APIRouter()


@router.get("/users", tags=["users"], response_model=list[UserDto])
async def read_users(session: Session = Depends(get_db), user: User = Depends(jwt_filter)):
    return users_service.get_users(session)


@router.get("/users/{user_id}", tags=["users"], response_model=UserDto)
async def get_one_user_by_id(user_id: int, session: Session = Depends(get_db)):
    return users_service.get_one_user_by_id(user_id=user_id, session=session)


@router.post("/users", tags=["users"], response_model=Union[UserDto, None])
async def create_user(create_user_dto: CreateUserDto, session: Session = Depends(get_db)):
    return users_service.create_user(create_user_dto=create_user_dto, session=session)


@router.put("/users/{user_id}", tags=["users"], response_model=Union[UserDto, None])
async def update_user(user_id: int, create_user_dto: CreateUserDto, session: Session = Depends(get_db)):
    return users_service.update_user(user_id=user_id, create_user_dto=create_user_dto, session=session)
