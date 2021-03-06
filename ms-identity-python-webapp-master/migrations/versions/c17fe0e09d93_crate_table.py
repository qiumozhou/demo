"""crate table

Revision ID: c17fe0e09d93
Revises: 
Create Date: 2020-08-20 11:41:13.774516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c17fe0e09d93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_user',
    sa.Column('is_delete', sa.BOOLEAN(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=True),
    sa.Column('middlename', sa.String(length=20), nullable=True),
    sa.Column('lastname', sa.String(length=20), nullable=True),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('otherphone', sa.String(length=12), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('is_commited', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_user')
    # ### end Alembic commands ###
