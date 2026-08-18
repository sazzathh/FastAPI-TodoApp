"""phone number column adding for our user table

Revision ID: 3ca69cf620f9
Revises: 
Create Date: 2026-08-18 00:18:17.746555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ca69cf620f9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone_number",sa.String(20),nullable=True))


def downgrade() -> None:
    op.drop_column("users","phone_number")
