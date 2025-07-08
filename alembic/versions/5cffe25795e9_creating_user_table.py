"""creating user table

Revision ID: 5cffe25795e9
Revises: 8978f56d9276
Create Date: 2025-07-08 13:18:51.981350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision: str = '5cffe25795e9'
down_revision: Union[str, Sequence[str], None] = '8978f56d9276'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id",sa.String,primary_key=True,nullable=False),
                    sa.Column(
                        "email",sa.String,nullable=False,unique=True
                    ),
                    sa.Column("password",sa.String,nullable=False),
                    sa.Column("created_at",sa.DateTime(timezone=True),server_default=func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
