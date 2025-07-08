"""adding colum owner_id and foreign key to post table

Revision ID: 50b5f216e5e5
Revises: 5cffe25795e9
Create Date: 2025-07-08 13:31:55.241226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50b5f216e5e5'
down_revision: Union[str, Sequence[str], None] = '5cffe25795e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",
        sa.Column("owner_id",sa.String,nullable=False))
    op.create_foreign_key("posts_user_fkey",source_table="posts", referent_table="users",local_cols=["owner_id"],remote_cols=["id"],
                          ondelete="CASCADE")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_user_fkey",table_name="posts")
    op.drop_column("posts","owner_id")
   
