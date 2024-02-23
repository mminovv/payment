from fastapi import APIRouter
from src.api.controllers.auth import auth
from src.api.controllers.payment import payment


def bind_routes():
    router = APIRouter(prefix='/api')
    router.include_router(auth)
    router.include_router(payment)
    return router
