from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler # noqa

from src.api.exceptions.handler import (
    access_denied_error_handler,
    auth_error_handler,
    logic_error_handler,
    not_found_error_handler,
    token_expired_or_not_valid,
)
from src.services.auth.exceptions import (
    TokenExpiredOrNotValid,
    AuthenticationError,
    AccessDeniedError,
)
from src.services.exceptions import RateLimitException
from src.services.users.exceptions import (
    UserNotFoundError,
)


def register_exceptions(app: FastAPI) -> None:
    app.exception_handlers.setdefault(
        TokenExpiredOrNotValid, token_expired_or_not_valid,
    )
    app.exception_handlers.setdefault(
        AuthenticationError, auth_error_handler,
    )
    app.exception_handlers.setdefault(
        AccessDeniedError, access_denied_error_handler,
    )
    app.exception_handlers.setdefault(
        UserNotFoundError, not_found_error_handler,
    )
    app.exception_handlers.setdefault(
        ValueError, logic_error_handler,
    )
    app.exception_handlers.setdefault(
        RateLimitException, _rate_limit_exceeded_handler,
    )
