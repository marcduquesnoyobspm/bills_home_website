"""change collation

Revision ID: 79214ac6e915
Revises: c702d37e9658
Create Date: 2023-03-25 21:53:51.338408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79214ac6e915'
down_revision = 'c702d37e9658'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_identifiant', sa.String(length=60, collation='utf8_bin'), nullable=True),
    sa.Column('user_email', sa.String(length=60), nullable=True),
    sa.Column('user_password', sa.String(length=60), nullable=True),
    sa.Column('user_firstname', sa.String(length=60), nullable=True),
    sa.Column('user_lastname', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('user_identifiant')
    )
    op.create_table('contract',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_mens', sa.Float(), nullable=False),
    sa.Column('contract_date', sa.Date(), nullable=False),
    sa.Column('contract_category', sa.String(length=60), nullable=True),
    sa.Column('contract_name', sa.String(length=60), nullable=True),
    sa.Column('contract_entreprise', sa.String(length=60), nullable=True),
    sa.Column('contract_url', sa.String(length=60), nullable=True),
    sa.Column('contract_identifiant', sa.String(length=255), nullable=True),
    sa.Column('contract_password', sa.String(length=255), nullable=True),
    sa.Column('contract_num', sa.String(length=255), nullable=True),
    sa.Column('contract_more_infos', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contract')
    op.drop_table('user')
    # ### end Alembic commands ###