"""table3

Revision ID: 21de853aefce
Revises: d27bdb96639e
Create Date: 2020-08-21 09:48:55.217723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21de853aefce'
down_revision = 'd27bdb96639e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_user', sa.Column('contact_id', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_user', 'contact_id')
    # ### end Alembic commands ###