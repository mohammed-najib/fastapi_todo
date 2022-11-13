"""create address_id to users

Revision ID: 83531e5c7b98
Revises: db336cb785db
Create Date: 2022-11-13 22:48:17.801550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83531e5c7b98"
down_revision = "db336cb785db"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "address_id",
            sa.Integer(),
            nullable=True,
        ),
    )
    op.create_foreign_key(
        "address_users_fk",
        source_table="users",
        referent_table="address",
        local_cols=["address_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint(
        "address_users_fk",
        table_name="users",
    )
    op.drop_column(
        "users",
        "address_id",
    )
