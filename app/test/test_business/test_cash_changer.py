from unittest import TestCase

from ...main.business.cash_changer import CashChanger


class TestCashChange(TestCase):
    def test_cash_changer_calculator(self):
        result = CashChanger().cash_changer_calculator(product_value=111.11, client_cash=222.22)

        expect = {
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
