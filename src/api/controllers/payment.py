from fastapi import (
    APIRouter,
    Depends,
)

from src.interfaces.db import get_session
from src.interfaces.repositories.db.balance import IBalanceRepository
from src.interfaces.repositories.db.transactions import ITransactionsRepository
from src.services.common import get_current_user
from src.services.payment.dto.request import PaymentRequest
from src.services.payment.dto.response import PaymentResponse
from src.services.payment.use_case import PaymentUseCase

payment = APIRouter(prefix='/payment', tags=['payment'])


@payment.post('/withdrawal', response_model=PaymentResponse)
async def payment_withdraw(
    dto: PaymentRequest,
    session: get_session = Depends(),
    balance_repo: IBalanceRepository = Depends(),
    user: get_current_user = Depends(),
    transaction_repo: ITransactionsRepository = Depends(),
):
    use_case = PaymentUseCase(
        session=session,
        transaction_repo=transaction_repo,
        balance_repo=balance_repo
    )
    return await use_case(dto=dto, user=user)
