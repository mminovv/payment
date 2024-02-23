from pydantic import BaseModel

from src.core.enums.transaction_reason import TransactionReasonEnum


class PaymentRequest(BaseModel):
    amount: int
    description: str
    reason_type: TransactionReasonEnum

