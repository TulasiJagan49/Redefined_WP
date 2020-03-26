"""Added id column to users database

Revision ID: 92259da0aa6d
Revises: 9f82fe1426a5
Create Date: 2020-03-26 20:36:34.906785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92259da0aa6d'
down_revision = '9f82fe1426a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'id')
    # ### end Alembic commands ###