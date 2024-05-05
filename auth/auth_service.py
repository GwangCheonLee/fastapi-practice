from datetime import timedelta

from fastapi import HTTPException

from auth.dto.sign_in_dto import SignInDto
from auth.models.auth_model import SignInResponse
from common.constatns import verify_password
from common.jwt_provider import create_access_token
from config.database import Session, setting
from users.dto.user_dto import UserDto
from users.repositories.user_repository import UserRepository


def sign_in(sign_in_dto: SignInDto, session: Session) -> SignInResponse:
    user_repo: UserRepository = UserRepository(session)
    user: UserDto = user_repo.get_one_user_by_email(email=sign_in_dto.email)

    is_password_valid: bool = verify_password(sign_in_dto.password, user.password)
    if is_password_valid:
        access_token = create_access_token(data={"user": {"email": user.email, "id": user.id, "name": user.name}},
                                           expires_delta=timedelta(minutes=setting.jwt_expires),
                                           secret_key=setting.jwt_secret, algorithm=setting.jwt_algorithm)

        return SignInResponse(access_token=access_token)
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
