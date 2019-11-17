from http import HTTPStatus

from flask import request
from flask_restplus import Resource

from ..service.transactions_service import create_transaction
from ..utils.dto import TransactionsDTO

api = TransactionsDTO.api
_transaction = TransactionsDTO.transaction


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
