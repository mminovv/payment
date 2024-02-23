from os import environ

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_URI = environ.get('POSTGRES_URI')
    SECRET_KEY = environ.get('SECRET_KEY')
    EXPIRE_MINUTES: int = environ.get('EXPIRE_MINUTES', default=5)
    ALGORITHM = environ.get('ALGORITHM')
    REDIS_URL: str = environ.get('REDIS_URL')
    LIMITER_REQUESTS: str = environ.get('LIMITER_REQUESTS', default='5/3minute')
    LIMITER_ENABLED: bool = environ.get('LIMITER_ENABLED', default=False)


settings = Settings()
