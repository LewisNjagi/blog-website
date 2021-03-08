"""Added Subscribers table

Revision ID: faf682febf3c
Revises: 26122d9046c4
Create Date: 2021-03-08 20:24:35.783538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faf682febf3c'
down_revision = '26122d9046c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_subscribers_email', table_name='subscribers')
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.create_index('ix_subscribers_email', 'subscribers', ['email'], unique=False)
    # ### end Alembic commands ###