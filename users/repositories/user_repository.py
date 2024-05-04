from config.database import Session
from models.user import User
from users.dto.user_dto import UserDto


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> list[UserDto]:
        users: list[User] = self.session.query(User).all()
        return [user.to_dto() for user in users]

    def get_one_user_by_id(self, user_id: int) -> UserDto:
        user: User = self.session.query(User).filter(User.id == user_id).one()
        return user.to_dto()
