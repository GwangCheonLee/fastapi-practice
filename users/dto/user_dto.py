from pydantic import BaseModel


class BaseUserDto(BaseModel):
    name: str
    email: str
    password: str


class UserDto(BaseUserDto):
    id: int


class CreateUserDto(BaseUserDto):
    pass
