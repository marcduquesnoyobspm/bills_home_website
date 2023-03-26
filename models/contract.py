import sqlalchemy as sa
import datetime
from sqlalchemy import orm, ForeignKey
from cryptography.fernet import Fernet
from . import db

key = open("utils/key.txt").readline()
f_key = Fernet(key)

class Contract(db.Model):

    __tablename__ = "contract"

    id: orm.Mapped[int] = orm.mapped_column(primary_key = True)

    contract_category = sa.Column(sa.String(60))
    
    contract_name = sa.Column(sa.String(60))
    
    contract_entreprise = sa.Column(sa.String(60))
    
    contract_url = sa.Column(sa.String(60))

    contract_identifiant = sa.Column(sa.String(255))

    contract_password = sa.Column(sa.String(255)) 

    contract_num = sa.Column(sa.String(255))

    contract_mens: orm.Mapped[float]

    contract_date: orm.Mapped[datetime.date]

    contract_more_infos = sa.Column(sa.String(255))
    
    user_id: orm.Mapped[int] = orm.mapped_column(ForeignKey("user.id"))

    user: orm.Mapped["User"] = orm.relationship(back_populates = "contracts")
    
    contract_date_creation: orm.Mapped[datetime.date]
    
    contract_popularity = sa.Column(sa.Integer)
    
    def set_password(self, password):
        self.contract_password = f_key.encrypt(password.encode())

    def get_password(self):
        return f_key.decrypt(self.contract_password).decode()
    
    def set_identifiant(self, identifiant):
        self.contract_identifiant = f_key.encrypt(identifiant.encode())

    def get_identifiant(self):
        return f_key.decrypt(self.contract_identifiant).decode()
    
    def set_num(self, num):
        self.contract_num = f_key.encrypt(num.encode())

    def get_num(self):
        return f_key.decrypt(self.contract_num).decode()