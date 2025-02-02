"""update user table.

Revision ID: bc604ec82fbc
Revises: 465d0779025d
Create Date: 2025-01-17 16:48:20.073580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc604ec82fbc'
down_revision = '465d0779025d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=64), nullable=False))
        batch_op.drop_column('is_approved')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_approved', sa.BOOLEAN(), nullable=True))
        batch_op.drop_column('role')

    # ### end Alembic commands ###
