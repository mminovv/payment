from abc import (
    ABC,
    abstractmethod,
)

from src.infra.db import Transactions


class ITransactionsRepository(ABC):

    @abstractmethod
    async def create_transaction(self, instance: Transactions):
        raise NotImplementedError
