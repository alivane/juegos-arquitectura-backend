"""empty message

Revision ID: 132f794f7ed9
Revises: 
Create Date: 2020-12-06 17:31:41.237275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '132f794f7ed9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('avatars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('path_image', sa.String(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('helmets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('path_image', sa.String(), nullable=False),
    sa.Column('coins', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('levels',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mail', sa.String(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('coins', sa.Integer(), nullable=False),
    sa.Column('id_avatar', sa.Integer(), nullable=False),
    sa.Column('id_helmet', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_avatar'], ['avatars.id'], ),
    sa.ForeignKeyConstraint(['id_helmet'], ['helmets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('avatars_by_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_avatar', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_avatar'], ['avatars.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('helmets_by_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_helmet', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_helmet'], ['helmets.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('levels_by_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_level', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_level'], ['levels.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('levels_by_user')
    op.drop_table('helmets_by_user')
    op.drop_table('avatars_by_user')
    op.drop_table('users')
    op.drop_table('levels')
    op.drop_table('helmets')
    op.drop_table('avatars')
    # ### end Alembic commands ###