"""create address table

Revision ID: db336cb785db
Revises: c24f6dbbad64
Create Date: 2022-11-13 22:39:13.892587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "db336cb785db"
down_revision = "c24f6dbbad64"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            "address1",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "address2",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "city",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "state",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "country",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "postalcode",
            sa.String(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("address")
