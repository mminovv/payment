from enum import Enum


class TransactionReasonEnum(Enum):
    PAYMENT = "payment"
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    TRANSFER = "transfer"
