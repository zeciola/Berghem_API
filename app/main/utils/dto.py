from flask_restplus import Namespace, fields


class TransactionsDTO:
    api = Namespace('transaction', description='Cash change transaction')
    transaction = api.model('transaction', {
        'product_name': fields.String(required=True, description='transaction product name'),
        'product_value': fields.Float(required=True, description='transaction product value'),
        'client_cash': fields.Float(required=True, description='transaction client cash')
    })
    transaction_update_by_id = api.model('transaction_update_by_name', {
        'new_product_name': fields.String(required=True, description='transaction product name'),
        'transaction_id': fields.Integer(required=True, description='transaction id'),
    })
    transaction_delete_by_id = api.model('transaction_delete_by_id', {
        'transaction_id': fields.Integer(required=True, description='transaction id'),
    })
    transaction_list = api.model('transaction_list', {
        'product_name': fields.String(description='transaction product name'),
        'product_value': fields.Float(description='transaction product value'),
        'transaction_date': fields.DateTime(description='transaction transaction date'),
        'client_cash': fields.Float(description='transaction client cash'),
        'cash_change': fields.Float(description='transaction cash change'),
        'money_bills': fields.List(fields.Raw(description='transaction money bills'))
    })
