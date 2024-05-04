from config.database import Session
from models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> list[User]:
        return self.session.query(User).all()

    def get_one_user_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).one()
