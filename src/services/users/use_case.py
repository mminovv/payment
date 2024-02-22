import sqlalchemy

from src.core.security import hashing_secret
from src.infra.db import (
    User,
)
from src.interfaces.repositories.db.users import IUsersRepository
from src.services.common import CommonUseCase
from src.services.users.exceptions import UserAlreadyExistsOrNoSuchRoleSystemError


class UserCreateUseCase(CommonUseCase):

    def __init__(
        self,
        *args,
        repo: IUsersRepository,
        **kwargs,
    ):
        self.repo = repo
        super().__init__(*args, **kwargs)

    def __call__(
        self,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> User:
        with self.session:
            instance = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=hashing_secret(secret=password),
            )
            try:
                self.repo.insert_user(instance=instance)
                self.session.commit()
            except sqlalchemy.exc.IntegrityError:
                print(f'User already exists with username: {repr(username)}')
            return instance
