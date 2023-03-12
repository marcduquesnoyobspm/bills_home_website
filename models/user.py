import sqlalchemy as sa
from typing import List

from sqlalchemy import orm
from flaskr.database import db
from models.asso_user_contract import association_table


class User(db.Model):

    __tablename__ = "user"

    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)

    user_name = sa.Column(sa.String(60))

    user_password = sa.Column(sa.String(60))

    user_firstname = sa.Column(sa.String(60))

    user_lastname = sa.Column(sa.String(60))

    contracts: orm.Mapped[List["Contract"]] = orm.relationship(secondary = association_table, back_populates = "users")
