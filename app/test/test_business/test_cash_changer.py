import unittest

from app.test.flask_base_test import FlaskBaseTest

from app.main.business.cash_changer import CashChanger


class TestCashChange(FlaskBaseTest):
    def test_cash_changer_calculator(self):
        result = CashChanger().cash_changer_calculator(product_value=111.11, client_cash=222.22)

        expect = {
            'product_value': 111.11,
            'client_cash': 222.22,
            'cash_change': 111.11,
            'money_bills': [
                {'money_100.0': 1},
                {'money_10.0': 1},
                {'money_1.0': 1},
                {'money_0.1': 1},
                {'money_0.01': 1}
            ]
        }
        self.assertDictEqual(result, expect)

    def test_error_cash_changer_calculator_client_cash_is_low(self):
        result = CashChanger().cash_changer_calculator(product_value=1111.11, client_cash=222.22)

        expect = dict(error='customer money is not enough')
        self.assertDictEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
