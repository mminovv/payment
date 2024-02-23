from uuid import UUID

from sqlalchemy import update, func, Numeric

from src.infra.db import Balance
from src.infra.db.repositories.common import CommonRepository
from src.interfaces.repositories.db.balance import IBalanceRepository


class BalanceRepository(CommonRepository, IBalanceRepository):

    def add_balance(self, instance: Balance) -> None:
        self.session.add(instance)

    async def withdraw_funds(self, user_id: UUID, amount: float) -> None:
        query = (
            update(Balance)
            .where(Balance.user_id == user_id)
            .values(balance=amount)
            .returning(Balance.balance)
        )
        result = await self.session.execute(query)
        return result.scalar()
