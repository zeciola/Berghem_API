from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = config_by_name[config_name].SQLAlCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_by_name[config_name].SQLAlCHEMY_TRACK_MODIFICATIONS
    app.config['DEBUG'] = config_by_name[config_name].DEBUG
    db.init_app(app)
    return app
