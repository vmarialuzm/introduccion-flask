"""initial migration

Revision ID: 998f109c32ee
Revises: 
Create Date: 2023-04-11 15:38:43.386775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998f109c32ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('idAula', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'nombre', 'apellido', 'idAula')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alumno')
    # ### end Alembic commands ###