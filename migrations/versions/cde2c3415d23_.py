"""empty message

Revision ID: cde2c3415d23
Revises: 8c3170295491
Create Date: 2019-05-21 23:18:12.821075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cde2c3415d23'
down_revision = '8c3170295491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('name', sa.String()))
    op.create_index(op.f('ix_questions_name'), 'questions', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_questions_name'), table_name='questions')
    op.drop_column('questions', 'name')
    # ### end Alembic commands ###
