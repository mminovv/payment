from abc import (
    ABC,
    abstractmethod,
)
from uuid import UUID

from src.infra.db import Balance


class IBalanceRepository(ABC):

    @abstractmethod
    def add_balance(self, instance: Balance) -> None:
        raise NotImplementedError

    @abstractmethod
    async def withdraw_funds(self, user_id: UUID, amount: float) -> None:
        raise NotImplementedError
