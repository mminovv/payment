from fastapi import APIRouter
from src.api.controllers.auth import auth


def bind_routes():
    router = APIRouter(prefix='/api')
    router.include_router(auth)
    return router
