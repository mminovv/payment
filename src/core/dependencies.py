from typing import TypeVar

from fastapi import (
    Depends,
    FastAPI,
)

from src.core.database import (
    async_session_impl,
)
from src.interfaces.db import (
    get_session,
)

T = TypeVar('T')


def override_repo(repo: T):
    def wrap(session: get_session = Depends()): return repo(session)

    return wrap


def register_dependencies(app: FastAPI):
    app.dependency_overrides.setdefault(
        *async_session_impl
    )
