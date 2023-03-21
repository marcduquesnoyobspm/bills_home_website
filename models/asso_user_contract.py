import sqlalchemy as sa
from . import db

association_table = db.Table(
    "association_table",
    sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), primary_key=True),
    sa.Column("contract_id", sa.Integer, sa.ForeignKey("contract.id"), primary_key=True)
)