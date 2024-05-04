from config.database import Session
from models import User
from users.repositories.user_repository import UserRepository


def get_users(session: Session) -> list[User]:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.get_users()


def get_one_user_by_id(session: Session, user_id: int) -> User:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.get_one_user_by_id(user_id)
