from sqlalchemy import Column, Integer, String

from schema import Base
from users.dto.user_dto import UserDto


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def to_dto(self):
        return UserDto(id=self.id, name=self.name, email=self.email, password=None)
