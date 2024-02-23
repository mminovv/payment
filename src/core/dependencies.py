from typing import TypeVar

from fastapi import (
    Depends,
    FastAPI,
)

from src.core.database import (
    async_session_impl,
)
from src.infra.db.repositories.balance import BalanceRepository
from src.infra.db.repositories.transaction import TransactionsRepository
from src.infra.db.repositories.users import UserRepository
from src.interfaces.db import (
    get_session,
)
from src.interfaces.repositories.db.balance import IBalanceRepository
from src.interfaces.repositories.db.transactions import ITransactionsRepository
from src.interfaces.repositories.db.users import IUsersRepository

T = TypeVar('T')


def override_repo(repo: T):
    def wrap(session: get_session = Depends()): return repo(session)

    return wrap


def register_dependencies(app: FastAPI):
    app.dependency_overrides.setdefault(
        *async_session_impl
    )
    app.dependency_overrides.setdefault(
        *(IUsersRepository, override_repo(UserRepository))
    )
    app.dependency_overrides.setdefault(
        *(IBalanceRepository, override_repo(BalanceRepository))
    )
    app.dependency_overrides.setdefault(
        *(ITransactionsRepository, override_repo(TransactionsRepository))
    )
