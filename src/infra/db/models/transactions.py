import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as psql

from src.core.enums.transaction_reason import TransactionReasonEnum
from src.core.enums.transaction_status import TransactionStatusEnum
from src.infra.db.models.common import Base


class Transactions(Base):
    __tablename__ = 'transactions'

    user_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    amount = sa.Column(
        sa.Numeric,
        nullable=False,
    )
    description = sa.Column(
        sa.String,
        nullable=True,
    )
    status = sa.Column(
        sa.Enum(TransactionStatusEnum),
        default=TransactionStatusEnum.PENDING,
        nullable=False,
    )
    reason = sa.Column(
        sa.Enum(TransactionReasonEnum),
        default=TransactionReasonEnum.PAYMENT,
        nullable=True,
    )
