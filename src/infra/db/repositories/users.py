from uuid import UUID

from sqlalchemy import select

from src.infra.db import User
from src.infra.db.repositories.common import CommonRepository
from src.interfaces.repositories.db.users import IUsersRepository


class UserRepository(CommonRepository, IUsersRepository):

    def insert_user(self, instance: User) -> User:
        return self.insert(instance=instance)

    async def get_user(self, condition):
        query = select(User).where(condition)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_user_by_username(self, username: str):
        return await self.get_user(User.username == username)

    async def get_user_by_id(self, user_id: UUID):
        return await self.get_user(User.id == user_id)
