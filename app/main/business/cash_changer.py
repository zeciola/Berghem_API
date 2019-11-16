from dataclasses import dataclass


@dataclass
class CashChanger:
    money = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

    def cash_changer_calculator(self, product_value: float, client_cash: float):
        self.money = sorted(self.money, reverse=True)
        if not client_cash >= product_value:
            return dict(error='customer money is not enough')

        cash_change = round(client_cash - product_value, 2)
        cash_change_view = cash_change
        cash_count = 0
        money_bills = []
        while cash_change > 0:
            for cash in self.money:
                while cash_change >= cash:
                    cash_change -= cash
                    cash_change = round(cash_change, 2)
                    cash_count += 1
                    if money_bills:
                        if {f'money_{cash}': cash_count}.keys() == money_bills[-1].keys():
                            money_bills[-1].update({f'money_{cash}': cash_count})
                        else:
                            money_bills.append({f'money_{cash}': cash_count})
                    else:
                        money_bills.append({f'money_{cash}': cash_count})
                cash_count = 0
        return dict(cash_change=cash_change_view, money_bills=money_bills)
