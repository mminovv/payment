from src.infra.db.models.common import Base, SoftDeleteMixin
import sqlalchemy as sa


class User(Base, SoftDeleteMixin):
    __tablename__ = 'users'

    username = sa.Column(
        sa.String,
        nullable=False,
        unique=True,
    )
    password = sa.Column(
        sa.String(60),
        nullable=False,
    )
    first_name = sa.Column(
        sa.String,
        nullable=True,
    )
    last_name = sa.Column(
        sa.String,
        nullable=True,
    )
