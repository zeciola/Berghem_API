from flask_restplus import Namespace, fields


class TransactionsDTO:
    api = Namespace('transaction', description='Cash change transaction')
    transaction = api.model('transaction', {
        'product_value': fields.Float(required=True, description='transaction product value'),
        'client_cash': fields.Float(required=True, description='transaction client cash'),
    })
