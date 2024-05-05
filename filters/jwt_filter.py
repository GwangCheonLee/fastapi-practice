from fastapi import Security, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from pydantic import parse_obj_as

from config.database import Session, get_db, setting
from users.dto.user_dto import UserDto
from users.repositories.user_repository import UserRepository

auth_scheme = HTTPBearer()


def jwt_filter(auth: HTTPAuthorizationCredentials = Security(auth_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(auth.credentials, setting.jwt_secret, algorithms=[setting.jwt_algorithm])
        user_data = payload.get("user")
        user_data["password"] = None
        user: UserDto = parse_obj_as(UserDto, user_data)

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid JWT token")

        user = UserRepository(db).get_one_user_by_id(user.id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
