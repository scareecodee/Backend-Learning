"""adding published colum to posts table

Revision ID: 54dcd2aaf8ca
Revises: 50b5f216e5e5
Create Date: 2025-07-08 19:56:37.465281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54dcd2aaf8ca'
down_revision: Union[str, Sequence[str], None] = '50b5f216e5e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("published",sa.Boolean,nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    pass
