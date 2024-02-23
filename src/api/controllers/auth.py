from fastapi import (
    APIRouter,
    Depends,
)

from starlette.responses import Response
from starlette.requests import Request


from src.interfaces.repositories.db.users import IUsersRepository
from src.services.auth.dto.request import UserLoginRequest
from src.services.auth.use_case import AuthorizationUseCase, AuthLogoutUseCase
from src.services.common import get_current_user, limiter

auth = APIRouter(prefix='/auth', tags=['auth'])


@auth.post('/login')
@limiter.limit("5/3minute")
async def login(
    request: Request, # noqa
    dto: UserLoginRequest,
    repo: IUsersRepository = Depends(),
):
    use_case = AuthorizationUseCase(repo=repo)
    return await use_case.authenticate(dto=dto, response=Response())


@auth.post('/logout')
async def logout(
    _: get_current_user = Depends()
):
    use_case = AuthLogoutUseCase()
    return await use_case.logout()
