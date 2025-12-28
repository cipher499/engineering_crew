import unittest

class Account:
    def __init__(self, user_id: str, initial_deposit: float) -> None:
        self.user_id = user_id
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
        self.initial_deposit = initial_deposit
        self.log_transaction('Deposit', initial_deposit)

    def log_transaction(self, action: str, amount: float, symbol: str = None, quantity: int = None):
        transaction = {'action': action, 'amount': amount}
        if symbol and quantity:
            transaction['symbol'] = symbol
            transaction['quantity'] = quantity
        self.transactions.append(transaction)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
        self.log_transaction('Deposit', amount)

    def withdraw(self, amount: float) -> None:
        if self._check_negative_balance(amount):
            raise ValueError('Insufficient funds for withdrawal.')
        self.balance -= amount
        self.log_transaction('Withdraw', amount)

    def buy_stock(self, symbol: str, quantity: int) -> None:
        if not self._check_affordable_stock(symbol, quantity):
            raise ValueError('Insufficient funds to buy stock.')
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.balance -= self.get_share_price(symbol) * quantity
        self.log_transaction('Buy', self.get_share_price(symbol) * quantity, symbol, quantity)

    def sell_stock(self, symbol: str, quantity: int) -> None:
        if not self._check_stock_availability(symbol, quantity):
            raise ValueError('Not enough shares to sell.')
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.balance += self.get_share_price(symbol) * quantity
        self.log_transaction('Sell', self.get_share_price(symbol) * quantity, symbol, quantity)

    def get_total_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += self.get_share_price(symbol) * quantity
        return total_value

    def get_profit_loss(self) -> float:
        return self.get_total_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions

    def _check_negative_balance(self, amount: float) -> bool:
        return self.balance - amount < 0

    def _check_affordable_stock(self, symbol: str, quantity: int) -> bool:
        return self.get_share_price(symbol) * quantity <= self.balance

    def _check_stock_availability(self, symbol: str, quantity: int) -> bool:
        return self.holdings.get(symbol, 0) >= quantity

    def get_share_price(self, symbol: str) -> float:
        prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
        return prices.get(symbol, 0.0)

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('user123', 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1100.0)

    def test_buy_stock(self):
        self.account.buy_stock('AAPL', 5)
        self.assertEqual(self.account.balance, 1000.0 - 5 * 150.0)
        self.assertEqual(self.account.get_holdings().get('AAPL'), 5)

    def test_buy_stock_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.buy_stock('AAPL', 10)

    def test_sell_stock(self):
        self.account.buy_stock('AAPL', 5)
        self.account.sell_stock('AAPL', 2)
        self.assertEqual(self.account.get_holdings().get('AAPL'), 3)
        self.assertEqual(self.account.balance, 1000.0 - 5 * 150.0 + 2 * 150.0)

    def test_sell_stock_not_enough_shares(self):
        with self.assertRaises(ValueError):
            self.account.sell_stock('AAPL', 10)

    def test_get_transactions(self):
        self.account.deposit(500.0)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 2)  # Initial deposit + deposit

    def test_get_profit_loss(self):
        self.account.deposit(500.0)
        self.account.buy_stock('AAPL', 5)
        self.assertGreater(self.account.get_profit_loss(), 0)

if __name__ == '__main__':
    unittest.main()