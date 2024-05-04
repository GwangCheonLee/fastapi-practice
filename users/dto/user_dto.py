from passlib.context import CryptContext
from pydantic import BaseModel, field_validator

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class BaseUserDto(BaseModel):
    name: str
    email: str
    password: str

    def hash_password(self):
        self.password = pwd_context.hash(self.password)


class UserDto(BaseUserDto):
    id: int


class CreateUserDto(BaseUserDto):
    @field_validator('password')
    def hash_password(cls, value):
        return pwd_context.hash(value)
