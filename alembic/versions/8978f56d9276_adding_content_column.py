"""adding content column

Revision ID: 8978f56d9276
Revises: a94280deece7
Create Date: 2025-07-08 13:06:58.135720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8978f56d9276'
down_revision: Union[str, Sequence[str], None] = 'a94280deece7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String,nullable=False))
   


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","content")
