"""create phone numbre for user col

Revision ID: c24f6dbbad64
Revises: 
Create Date: 2022-11-13 22:22:27.809283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c24f6dbbad64"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
