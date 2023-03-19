"""adding user_identifiant

Revision ID: 72773b5ff3c4
Revises: 8d6b9bf38f52
Create Date: 2023-03-19 12:28:55.856614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72773b5ff3c4'
down_revision = '8d6b9bf38f52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_identifiant', sa.String(length=60), nullable=True))
        batch_op.create_unique_constraint(None, ['user_identifiant'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_identifiant')

    # ### end Alembic commands ###
