import sqlalchemy as sa
import datetime

from typing import List
from sqlalchemy import orm
from .asso_user_contract import association_table
from . import db


class Contract(db.Model):

    __tablename__ = "contract"

    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)

    contract_name = sa.Column(sa.String(60))

    contract_identifiant = sa.Column(sa.String(60))

    contract_password = sa.Column(sa.String(60))

    contract_url = sa.Column(sa.String(60))

    contract_num = sa.Column(sa.String(60))

    contract_mens: orm.Mapped[float]

    contract_date: orm.Mapped[datetime.date]

    contract_more_infos = sa.Column(sa.String(60))

    users: orm.Mapped[List["User"]] = orm.relationship(secondary = association_table, back_populates = "contracts")