from datetime import datetime
from http import HTTPStatus

from app.main import db
from app.main.business.cash_changer import CashChanger
from app.main.model.transactions import Transactions


def delete_object(delete_data):
    db.session.delete(delete_data)
    db.session.commit()


def save_changes(commit_data):
    db.session.add(commit_data)
    db.session.commit()


def create_transaction(request_data: dict):
    product_value = request_data['product_value']
    client_cash = request_data['client_cash']
    product_name = request_data['product_name']

    result = CashChanger().cash_changer_calculator(product_value=product_value, client_cash=client_cash)

    if result.get('error'):
        return result, HTTPStatus.BAD_REQUEST

    cash_change = result['cash_change']
    money_bills = result['money_bills']

    new_transaction = Transactions(
        product_name = product_name,
        product_value = product_value,
        client_cash = client_cash,
        cash_change = cash_change,
        money_bills = money_bills
    )

    save_changes(commit_data=new_transaction)
    response_object = dict(
        status='success',
        msg='Transaction as confirmed',
        product_name=product_name,
        cash_change_calculator=result
    )

    return response_object, HTTPStatus.CREATED


def list_all_transactions():
    all_transactions = Transactions.query.all()
    return all_transactions, HTTPStatus.OK


def list_transaction_by_id(transaction_id: int):
    one_transaction = Transactions.query.filter_by(id=transaction_id).first()
    return one_transaction, HTTPStatus.OK


def update_product_name_by_id_transaction(request_data: dict):
    new_product_name = request_data['new_product_name']
    transaction_id = request_data['transaction_id']
    
    update_transaction = Transactions.query.filter_by(id=transaction_id).first()
    if not update_transaction:
        return dict(error='transaction id not found'), HTTPStatus.BAD_REQUEST

    update_transaction.product_name = new_product_name
    db.session.commit()

    return dict(
        status='success',
        msg=f'Transaction {transaction_id} was Updated',
        new_name=new_product_name
    ), HTTPStatus.OK


def delete_transaction_by_id(request_data: dict):
    transaction_id = request_data['transaction_id']

    delete_transaction = Transactions.query.filter_by(id=transaction_id).first()
    if not delete_transaction:
        return dict(error='transaction id not found')

    delete_object(delete_transaction)

    return dict(
        status='success',
        msg=f'Transaction {transaction_id} was Deleted'
    ), HTTPStatus.OK
