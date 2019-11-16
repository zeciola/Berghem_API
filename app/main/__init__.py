from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from .config import config_by_name

db = MongoAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['MONGOALCHEMY_DATABASE'] = config_by_name[config_name].MONGODB_SETTINGS['db']
    app.config['MONGOALCHEMY_CONNECTION_STRING'] = config_by_name[config_name].MONGODB_DATABASE_URI
    db.init_app(app)

    return app
