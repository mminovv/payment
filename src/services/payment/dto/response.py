from pydantic import BaseModel

from src.core.enums.transaction_status import TransactionStatusEnum


class PaymentResponse(BaseModel):
    status: TransactionStatusEnum
    description: str

