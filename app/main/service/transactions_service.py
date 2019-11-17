from http import HTTPStatus

from app.main import db
from app.main.business.cash_changer import CashChanger
from app.main.model.transactions import Transactions


def save_changes(commit_data):
    db.session.add(commit_data)
    db.session.commit()


def create_transaction(request_data: dict):
    product_value = request_data['product_value']
    client_cash = request_data['client_cash']

    result = CashChanger().cash_changer_calculator(product_value=product_value, client_cash=client_cash)

    if result.get('error'):
        return result, HTTPStatus.BAD_REQUEST

    cash_change = result['cash_change']
    money_bills = result['money_bills']

    new_transaction = Transactions(
        product_value=product_value,
        client_cash=client_cash,
        cash_change=cash_change,
        money_bills=money_bills
    )

    save_changes(commit_data=new_transaction)
    response_object = dict(
        status='success',
        msg='Transaction as confirmed',
        cash_change_calculator=result
    )

    return response_object, HTTPStatus.CREATED
