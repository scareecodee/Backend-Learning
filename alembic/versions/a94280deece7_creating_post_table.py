"""creating post table

Revision ID: a94280deece7
Revises: 
Create Date: 2025-07-08 09:34:25.669248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a94280deece7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",
                    sa.Column("id",sa.Integer,nullable=False,primary_key=True),
                    sa.Column("title",sa.String,nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("posts")

