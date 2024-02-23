from src.infra.db import Transactions
from src.infra.db.repositories.common import CommonRepository
from src.interfaces.repositories.db.transactions import ITransactionsRepository


class TransactionsRepository(CommonRepository, ITransactionsRepository):

    async def create_transaction(self, instance: Transactions):
        return self.insert(instance)
