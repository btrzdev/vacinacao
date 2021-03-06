"""Criação tabela Patient

Revision ID: 5f6b95921561
Revises: 
Create Date: 2022-04-13 07:53:42.062764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f6b95921561'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unit_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cpf'),
    sa.CheckConstraint('length("cpf")=11', name='regra_check_cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient')
    # ### end Alembic commands ###
