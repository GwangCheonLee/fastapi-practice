from sqlalchemy import Column, Integer, String

from config.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email}, password={self.password})>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "password": self.password}
