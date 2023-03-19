import sqlalchemy as sa
import datetime

from typing import List
from sqlalchemy import orm
from .asso_user_contract import association_table
from . import db, bcrypt


class Contract(db.Model):

    __tablename__ = "contract"

    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)

    contract_category = sa.Column(sa.String(60))
    
    contract_entreprise = sa.Column(sa.String(60))

    contract_identifiant = sa.Column(sa.String(60))

    contract_password = sa.Column(sa.String(60))

    contract_url = sa.Column(sa.String(60))

    contract_num = sa.Column(sa.String(60))

    contract_mens: orm.Mapped[float]

    contract_date: orm.Mapped[datetime.date]

    contract_more_infos = sa.Column(sa.String(60))

    users: orm.Mapped[List["User"]] = orm.relationship(secondary = association_table, back_populates = "contracts")
    
    def set_password(self, password):
        self.contract_password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.contract_password, password)
    
    def set_identifiant(self, identifiant):
        self.contract_identifiant = bcrypt.generate_password_hash(identifiant).decode("utf-8")

    def check_identifiant(self, identifiant):
        return bcrypt.check_password_hash(self.contract_identifiant, identifiant)
    
    def set_num(self, num):
        self.contract_num = bcrypt.generate_password_hash(num).decode("utf-8")

    def check_num(self, num):
        return bcrypt.check_password_hash(self.contract_num, num)