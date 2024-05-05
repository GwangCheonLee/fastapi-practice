from config.database import Session
from models.user import User
from users.dto.user_dto import UserDto, CreateUserDto


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> list[UserDto]:
        users: list[User] = self.session.query(User).all()
        return [user.to_dto() for user in users]

    def get_one_user_by_id(self, user_id: int) -> UserDto:
        user: User = self.session.query(User).filter(User.id == user_id).one()
        return user.to_dto()

    @staticmethod
    def save_user(create_user_dto: CreateUserDto, session: Session) -> UserDto:
        user = User(
            name=create_user_dto.name,
            email=create_user_dto.email,
            password=create_user_dto.password
        )

        session.add(user)
        session.commit()
        return user.to_dto()

    @staticmethod
    def update_user(user_id: int, create_user_dto: CreateUserDto, session: Session) -> UserDto:
        user = session.query(User).filter(User.id == user_id).one()
        user.name = create_user_dto.name
        user.email = create_user_dto.email
        user.password = create_user_dto.password

        session.commit()
        return user.to_dto()
