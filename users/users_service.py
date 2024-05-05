from config.database import Session
from users.dto.user_dto import UserDto, CreateUserDto
from users.repositories.user_repository import UserRepository


def get_users(session: Session) -> list[UserDto]:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.get_users()


def get_one_user_by_id(session: Session, user_id: int) -> UserDto:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.get_one_user_by_id(user_id)


def create_user(create_user_dto: CreateUserDto, session: Session) -> UserDto:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.save_user(create_user_dto, session)


def update_user(user_id: int, create_user_dto: CreateUserDto, session: Session) -> UserDto:
    userRepository: UserRepository = UserRepository(session)
    return userRepository.update_user(user_id=user_id, create_user_dto=create_user_dto, session=session)
