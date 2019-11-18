import unittest
from http import HTTPStatus

from app.test.flask_base_test import FlaskBaseTest


class TestTransactionsCashChange(FlaskBaseTest):

    def test_transactions_cash_change_post(self):
        result = self.client.post(
            'api/transaction/cash_change',
            json={
                "product_name": 'Test Notebook',
                "product_value": 111.11,
                "client_cash": 222.22
            }
        )

        self.assertStatus(result, HTTPStatus.CREATED)

        expect = {
            "status": "success",
            "msg": "Transaction as confirmed",
            "product_name": "Test Notebook",
            "cash_change_calculator": {
                "product_value": 111.11,
                "client_cash": 222.22,
                "cash_change": 111.11,
                "money_bills": [
                    {
                        "money_100.0": 1
                    },
                    {
                        "money_10.0": 1
                    },
                    {
                        "money_1.0": 1
                    },
                    {
                        "money_0.1": 1
                    },
                    {
                        "money_0.01": 1
                    }
                ]
            }
        }

        self.assertDictEqual(result.json, expect)

    def test_transaction_cash_change_more_cash_post(self):
        result = self.client.post(
            'api/transaction/cash_change',
            json={
                "product_value": 5458.54,
                "client_cash": 7985.12
            }
        )

        self.assertStatus(result, HTTPStatus.CREATED)

        expect = {
            "status": "success",
            "msg": "Transaction as confirmed",
            "product_name": "dasadasd dWW",
            "cash_change_calculator": {
                "product_value": 5458.54,
                "client_cash": 7985.12,
                "cash_change": 2526.58,
                "money_bills": [
                    {
                        "money_100.0": 25
                    },
                    {
                        "money_20.0": 1
                    },
                    {
                        "money_5.0": 1
                    },
                    {
                        "money_1.0": 1
                    },
                    {
                        "money_0.5": 1
                    },
                    {
                        "money_0.05": 1
                    },
                    {
                        "money_0.01": 3
                    }
                ]
            }
        }

        self.assertDictEqual(result.json, expect)

    def test_transactions_cash_change_error_client_with_low_money_post(self):
        result = self.client.post(
            'api/transaction/cash_change',
            json={
                "product_value": 1100,
                "client_cash": 200
            }
        )

        self.assertStatus(result, HTTPStatus.BAD_REQUEST)

        expect = {'error': 'customer money is not enough'}

        self.assertDictEqual(result.json, expect)

    def test_transactions_cash_change_error_missing_fields_post(self):
        result = self.client.post(
            'api/transaction/cash_change',
            json={
                "product_value": 1100,
                # "client_cash": 200
            }
        )

        self.assertStatus(result, HTTPStatus.BAD_REQUEST)

        expect = {
            'errors':
                {
                    'client_cash': "'client_cash' is a required property"
                }, 'message': 'Input payload validation failed'
        }

        self.assertDictEqual(result.json, expect)

        result = self.client.post(
            'api/transaction/cash_change',
            json={
                # "product_value": 1100,
                "client_cash": 200
            }
        )

        self.assertStatus(result, HTTPStatus.BAD_REQUEST)

        expect = {
            'errors':
                {
                    'product_value': "'product_value' is a required property"
                }, 'message': 'Input payload validation failed'
        }

        self.assertDictEqual(result.json, expect)

    def test_transactions_list_all(self):
        self.create_transaction()
        self.create_transaction()
        self.create_transaction()

        result = self.client.get(
            'api/transaction/list',
        )

        self.assertStatus(result, HTTPStatus.OK)

        self.assertEqual(len(result.json), 3)

    def test_transactions_update(self):
        self.create_transaction()

        payload = {
            "new_product_name": "Teste",
            "transaction_id": 1
        }

        result = self.client.put(
            '/api/transaction/product_name/update',
            json=payload
        )

        self.assertStatus(result, HTTPStatus.OK)

        expect = dict(
            status='success',
            msg=f'Transaction {payload["transaction_id"]} was Updated',
            new_name=payload['new_product_name']
        )

        self.assertDictEqual(result.json, expect)
        ...

    def test_transactions_delete(self):
        self.create_transaction()

        payload = {
            "transaction_id": 1
        }

        result = self.client.delete(
            '/api/transaction/delete',
            json=payload
        )

        self.assertStatus(result, HTTPStatus.OK)

        expect = dict(
            status='success',
            msg=f'Transaction {payload["transaction_id"]} was Deleted'
        )

        self.assertDictEqual(result.json, expect)


if __name__ == '__main__':
    unittest.main()
