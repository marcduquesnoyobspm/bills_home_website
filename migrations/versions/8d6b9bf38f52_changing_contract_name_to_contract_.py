"""changing contract_name to contract_category

Revision ID: 8d6b9bf38f52
Revises: 4cddfe764f5f
Create Date: 2023-03-19 12:27:40.569809

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d6b9bf38f52'
down_revision = '4cddfe764f5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contract', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contract_category', sa.String(length=60), nullable=True))
        batch_op.drop_column('contract_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contract', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contract_name', mysql.VARCHAR(length=60), nullable=True))
        batch_op.drop_column('contract_category')

    # ### end Alembic commands ###