from fastapi import (
    Depends,
    Security,
)
from fastapi.security import APIKeyCookie
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import security
from src.infra.db import User
from src.interfaces.repositories.db.users import IUsersRepository
from src.services.auth.exceptions import TokenExpiredOrNotValid
from src.services.users.exceptions import UserNotFoundError

oauth2_scheme = APIKeyCookie(name='access_token')


async def get_current_user(
    token: str = Security(oauth2_scheme), user_repo: IUsersRepository = Depends()
) -> User:
    try:
        user_id = await security.decode_jwt_token(token)
        if user := await user_repo.get_user_by_id(user_id=user_id):
            return user
        raise UserNotFoundError
    except ValueError:
        raise TokenExpiredOrNotValid


class CommonUseCase:

    def __init__(self, session: AsyncSession = None, **kwargs):
        self.session = session
