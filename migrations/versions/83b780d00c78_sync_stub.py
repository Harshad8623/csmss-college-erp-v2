"""revision 83b780d00c78 stub for alembic sync

Revision ID: 83b780d00c78
Revises: 3125ee17c929
Create Date: 2026-05-18 13:15:23.716650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83b780d00c78'
down_revision = '3125ee17c929'
branch_labels = None
depends_on = None


def upgrade():
    # Pass without errors if tables/columns are already managed
    pass


def downgrade():
    pass
