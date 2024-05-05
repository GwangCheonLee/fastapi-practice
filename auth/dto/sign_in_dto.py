from pydantic import BaseModel


class SignInDto(BaseModel):
    email: str
    password: str
