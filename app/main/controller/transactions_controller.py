from http import HTTPStatus

from flask import request
from flask_restplus import Resource

from app.main.service.transactions_service import (create_transaction, update_product_name_by_id_transaction,
                                                   delete_transaction_by_id, list_all_transactions,
                                                   list_transaction_by_id)
from app.main.utils.dto import TransactionsDTO

api = TransactionsDTO.api
_transaction = TransactionsDTO.transaction
_transaction_update_by_id = TransactionsDTO.transaction_update_by_id
_transaction_delete_by_id = TransactionsDTO.transaction_delete_by_id
_transaction_list = TransactionsDTO.transaction_list


@api.route('/')
class DefaultRoute(Resource):

    @api.doc('Default Route on API')
    def get(self):
        '''Default Route on API'''
        return {'API': 'ON'}, HTTPStatus.OK


@api.route('/transaction/cash_change')
class TransactionsCashChange(Resource):

    @api.doc('Cash change calculator')
    @api.expect(_transaction, validate=True)
    def post(self):
        '''Cash change calculator'''
        payload = request.json
        return create_transaction(request_data=payload)


@api.route('/transaction/list')
class TransactionsListAll(Resource):

    @api.doc('List all transactions')
    @api.marshal_with(_transaction_list)
    def get(self):
        '''List all transactions'''
        return list_all_transactions()


@api.route('/transaction/list/<transaction_id>')
@api.param('transaction_id', 'Transaction ID')
class TransactionsListID(Resource):

    @api.doc('List by id transactions')
    @api.marshal_with(_transaction_list)
    def get(self, transaction_id: int):
        '''List by id transactions'''
        return list_transaction_by_id(transaction_id=transaction_id)


@api.route('/transaction/product_name/update')
class TransactionsUpdate(Resource):

    @api.doc('Update transaction product name by id')
    @api.expect(_transaction_update_by_id, validate=True)
    def put(self):
        '''Update transaction product name by id'''
        payload = request.json
        return update_product_name_by_id_transaction(request_data=payload)


@api.route('/transaction/delete')
class TransactionsDelete(Resource):

    @api.doc('Delete transaction by id')
    @api.expect(_transaction_delete_by_id, validate=True)
    def delete(self):
        '''Delete transaction by id'''
        payload = request.json
        return delete_transaction_by_id(request_data=payload)
