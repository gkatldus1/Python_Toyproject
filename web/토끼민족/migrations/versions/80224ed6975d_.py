"""empty message

Revision ID: 80224ed6975d
Revises: 
Create Date: 2021-07-14 16:26:37.362293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80224ed6975d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rabbitStore',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('open_time', sa.String(length=5), nullable=True),
    sa.Column('close_time', sa.String(length=5), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('thumbnail', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rabbitUser',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('point', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('telephone', sa.String(length=11), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rabbitMenu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('food_name', sa.String(length=20), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('thumbnail', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['rabbitStore.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rabbitReview',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['rabbitStore.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['rabbitUser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rabbitReview')
    op.drop_table('rabbitMenu')
    op.drop_table('rabbitUser')
    op.drop_table('rabbitStore')
    # ### end Alembic commands ###
