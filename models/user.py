import sqlalchemy as sa
from typing import List
import datetime
from sqlalchemy import orm
from flask_login import UserMixin

from . import db, bcrypt


class User(UserMixin, db.Model):

    __tablename__ = "user"

    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)
    
    user_identifiant = sa.Column(sa.String(60, collation = 'utf8_bin'), unique = True)

    user_email = sa.Column(sa.String(60), unique = True)

    user_password = sa.Column(sa.String(60))

    user_firstname = sa.Column(sa.String(60))

    user_lastname = sa.Column(sa.String(60))
    
    user_creation_date: orm.Mapped[datetime.date] = orm.mapped_column(nullable=True)

    contracts: orm.Mapped[List["Contract"]] = orm.relationship(back_populates = "user", cascade="all, delete")
    
    def set_password(self, password):
        self.user_password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

