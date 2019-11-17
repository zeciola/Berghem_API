from flask import Blueprint
from flask_restplus import Api

from app.main.controller.transactions_controller import api as transactions_api

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Berghem API Cash Changer',
    version='0.0.1',
    description='a boilerplate for flask restplus web service'
)

api.add_namespace(transactions_api, path='/api')
