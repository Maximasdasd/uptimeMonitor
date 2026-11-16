"""seed initial roles

Revision ID: 0e6bb249910f
Revises: ba739aa6fdaf
Create Date: 2026-11-14 09:38:19.032218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e6bb249910f'
down_revision: Union[str, Sequence[str], None] = 'ba739aa6fdaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    roles = sa.table(
        "role",
        sa.column("name", sa.String(length=255)),
    )

    op.bulk_insert(
        roles,
        [
            {"name": "user"},
            {"name": "admin"},
        ],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(sa.text("DELETE FROM role WHERE name IN ('user', 'admin');"))
