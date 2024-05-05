from fastapi import APIRouter, Depends

from auth import auth_service
from auth.dto.sign_in_dto import SignInDto
from auth.models.auth_model import SignInResponse
from config.database import Session, get_db

router = APIRouter(prefix="/auth")


@router.post("/sign-in", tags=["auth"], response_model=SignInResponse, status_code=200,
             responses={401: {"description": "Invalid email or password"}})
async def sign_up(sign_in_dto: SignInDto, session: Session = Depends(get_db)) -> SignInResponse:
    return auth_service.sign_in(sign_in_dto, session)
