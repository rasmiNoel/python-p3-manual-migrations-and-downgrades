"""Renaming students to scholars

Revision ID: bf223049018d
Revises: 791279dd0760
Create Date: 2023-12-17 16:58:20.077962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf223049018d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
