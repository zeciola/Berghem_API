from dataclasses import dataclass
from datetime import datetime

from .. import db


@dataclass
class Transactions(db.Model):
    """Transactions Model"""
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False, unique=True)
    product_value = db.Column(db.Float(), nullable=False)
    transaction_date = db.Column(db.DateTime(), default=datetime.utcnow())
    client_cash = db.Column(db.Float(), nullable=False)
    cash_change = db.Column(db.Float(), nullable=False)
    money_bills = db.Column(db.JSON(), nullable=False)

    def __repr__(self):
        return '<Transactions>'
