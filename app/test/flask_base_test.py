import random
import string

from flask_testing import TestCase

from app.main import db
from manage import app


class FlaskBaseTest(TestCase):
    """ Base Tests """

    def create_transaction(self):
        return self.client.post(
            'api/transaction/cash_change',
            json={
                "product_name": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
                "product_value": 10,
                "client_cash": 20
            }
        )
        ...

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
