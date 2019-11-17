from dataclasses import dataclass

from .. import db


@dataclass
class Transactions(db.Model):
    """Transactions Model"""
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_value = db.Column(db.Float(), nullable=False)
    client_cash = db.Column(db.Float(), nullable=False)
    cash_change = db.Column(db.Float(), nullable=False)
    money_bills = db.Column(db.JSON(), nullable=False)

    def __repr__(self):
        return '<Transactions>'
