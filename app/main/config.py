import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'The secret key of the lords')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLAlCHEMY_DATABASE_URI = 'sqlite:////tmp/berghem_api.db'
    SQLAlCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLAlCHEMY_DATABASE_URI = 'sqlite:////tmp/berghem_api_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLAlCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # SQLAlCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'berghem_api.db')
    # PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLAlCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

secret_key = Config.SECRET_KEY
