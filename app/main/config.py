import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'The secret key of the lords')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'BerghemDB',
        'host': 'localhost',
        'port': '27017'
    }
    MONGODB_DATABASE_URI = f'mongodb://{MONGODB_SETTINGS["host"]}:{MONGODB_SETTINGS["port"]}/{MONGODB_SETTINGS["db"]}'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'BerghemDB',
        'host': 'localhost',
        'port': '27017'
    }
    MONGODB_DATABASE_URI = f'mongodb://{MONGODB_SETTINGS["host"]}:{MONGODB_SETTINGS["port"]}/{MONGODB_SETTINGS["db"]}'

class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'BerghemDB',
        'host': 'localhost',
        'port': '27017'
    }
    MONGODB_DATABASE_URI = f'mongodb://{MONGODB_SETTINGS["host"]}:{MONGODB_SETTINGS["port"]}/{MONGODB_SETTINGS["db"]}'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

secret_key = Config.SECRET_KEY