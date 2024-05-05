from typing import Union

import bcrypt
from pydantic import BaseModel, field_validator


class BaseUserDto(BaseModel):
    name: str
    email: str
    password: Union[str, None]

    def hash_password(cls, value):
        if value is None:
            return value
        return bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()


class UserDto(BaseUserDto):
    id: int


class CreateUserDto(BaseUserDto):
    @field_validator('password')
    def hash_password(cls, value):
        return bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()
