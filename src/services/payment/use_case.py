from loguru import logger

from src.core.enums.transaction_status import TransactionStatusEnum
from src.infra.db import User, Transactions
from src.interfaces.repositories.db.balance import IBalanceRepository
from src.interfaces.repositories.db.transactions import ITransactionsRepository
from src.services.common import CommonUseCase
from src.services.payment.dto.request import PaymentRequest
from src.services.payment.dto.response import PaymentResponse


class PaymentUseCase(CommonUseCase):

    def __init__(
        self,
        *args,
        transaction_repo: ITransactionsRepository,
        balance_repo: IBalanceRepository,
        **kwargs
    ) -> None:
        self.transaction_repo = transaction_repo
        self.balance_repo = balance_repo
        super().__init__(*args, **kwargs)

    async def __call__(self, user: User, dto: PaymentRequest):
        user_balance = user.balance

        if (
            not user_balance
            or user_balance.balance <= 0
            or dto.amount > user_balance.balance
        ):
            return PaymentResponse(
                status=TransactionStatusEnum.FAILED,
                description='Insufficient funds'
            )

        try:
            async with self.session:
                remains = user_balance.balance - dto.amount
                await self.balance_repo.withdraw_funds(user_id=user.id, amount=remains)
                transaction = Transactions(
                    amount=dto.amount,
                    user_id=user.id,
                    description=dto.description,
                    reason=dto.reason_type,
                    status=TransactionStatusEnum.SUCCESS,
                )
                await self.transaction_repo.create_transaction(instance=transaction)
                await self.session.commit()
        except Exception as err:
            logger.error(
                err.__str__(),
                exc_info=True,
                stack_info=True,
                extra={
                    'user_id': user.id,
                    'amount': dto.amount,
                    'reason': dto.reason_type,
                    'transaction_id': transaction.id if transaction else None
                }
            )
            await self.session.rollback()
            return PaymentResponse(
                status=TransactionStatusEnum.FAILED,
                description='A transaction error has occurred'
            )

        return PaymentResponse(
            status=TransactionStatusEnum.SUCCESS,
            description=f'Transaction completed successfully. Remaining balance: {remains}'
        )
