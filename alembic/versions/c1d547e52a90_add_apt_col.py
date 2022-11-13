"""add apt col

Revision ID: c1d547e52a90
Revises: 83531e5c7b98
Create Date: 2022-11-14 00:59:18.642529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c1d547e52a90"
down_revision = "83531e5c7b98"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "address",
        sa.Column(
            "apt_num",
            sa.Integer(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("address", "apt_num")
