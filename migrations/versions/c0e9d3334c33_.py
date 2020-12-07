"""empty message

Revision ID: c0e9d3334c33
Revises: 496491463a5b
Create Date: 2020-12-06 18:48:10.163436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0e9d3334c33'
down_revision = '496491463a5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('levels', sa.Column('path', sa.String(), nullable=False))
    op.drop_column('levels', 'levels')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('levels', sa.Column('levels', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('levels', 'path')
    # ### end Alembic commands ###