import sqlalchemy

from src.core.security import hashing_secret
from src.infra.db import (
    User, Balance,
)
from src.interfaces.repositories.db.balance import IBalanceRepository
from src.interfaces.repositories.db.users import IUsersRepository
from src.services.common import CommonUseCase


class UserCreateUseCase(CommonUseCase):

    def __init__(
        self,
        *args,
        repo: IUsersRepository,
        balance_repo: IBalanceRepository,
        **kwargs,
    ):
        self.repo = repo
        self.balance_repo = balance_repo
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
                self.session.flush()
                balance = Balance(user_id=instance.id)
                self.balance_repo.add_balance(instance=balance)
                self.session.commit()

            except sqlalchemy.exc.IntegrityError:
                print(f'User already exists with username: {repr(username)}')
            return instance
