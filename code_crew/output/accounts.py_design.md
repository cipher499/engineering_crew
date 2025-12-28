# Design for the Account Management System Module

## Module Name: `accounts.py`

### Class: `Account`

The `Account` class represents a user account in the trading simulation platform. It will manage user funds, transactions, and stock holdings.

#### Attributes:
- `user_id` (str): The unique identifier for the user.
- `balance` (float): The current balance in the user's account.
- `holdings` (dict): A dictionary mapping stock symbols to the quantity of shares owned.
- `transactions` (list): A list that records all transactions made by the user.
- `initial_deposit` (float): The amount of money initially deposited by the user.

#### Methods:

1. **`__init__(self, user_id: str, initial_deposit: float) -> None`**
   - Initializes a new Account instance.
   - Sets the user ID, initial deposit (also sets `balance`), and initializes empty holdings and transactions.

2. **`deposit(self, amount: float) -> None`**
   - Adds the specified amount to the account balance.
   - Logs the transaction.

3. **`withdraw(self, amount: float) -> None`**
   - Reduces the account balance by the specified amount, ensuring it does not lead to a negative balance.
   - Logs the transaction.

4. **`buy_stock(self, symbol: str, quantity: int) -> None`**
   - Buys a specified quantity of stock for the given symbol, ensuring the user can afford it.
   - Updates the holdings and account balance accordingly.
   - Logs the transaction.

5. **`sell_stock(self, symbol: str, quantity: int) -> None`**
   - Sells a specified quantity of stock for the given symbol, ensuring the user holds enough shares to sell.
   - Updates the holdings and account balance accordingly.
   - Logs the transaction.

6. **`get_total_portfolio_value(self) -> float`**
   - Calculates the total value of the user's portfolio by summing the value of all holdings based on current share prices.

7. **`get_profit_loss(self) -> float`**
   - Calculates the profit or loss from the initial deposit by comparing the current balance and the total value of the portfolio against the initial deposit.

8. **`get_holdings(self) -> dict`**
   - Returns the current holdings of the user in the format `{symbol: quantity}`.

9. **`get_transactions(self) -> list`**
   - Returns a list of all transactions made by the user, including deposits, withdrawals, buys, and sells.

10. **`_check_negative_balance(self, amount: float) -> bool`**
    - A helper method to determine if a withdrawal request would leave the balance negative.

11. **`_check_affordable_stock(self, symbol: str, quantity: int) -> bool`**
    - A helper method to check if the user can afford the stock purchase based on the current share price and the quantity.

12. **`_check_stock_availability(self, symbol: str, quantity: int) -> bool`**
    - A helper method to verify if the user has enough shares for the selling transaction.

## External Function:

### `get_share_price(symbol: str) -> float`
- A function that retrieves the current price of a stock based on the symbol.
- This function will return fixed prices for test purposes:
  - `AAPL` => 150.00
  - `TSLA` => 700.00
  - `GOOGL` => 2800.00

### Example Usage:
- Create an account: `account = Account("user123", 1000.0)`
- Deposit funds: `account.deposit(500.0)`
- Withdraw funds: `account.withdraw(200.0)`
- Buy shares: `account.buy_stock("AAPL", 5)`
- Sell shares: `account.sell_stock("AAPL", 2)`
- Get portfolio value: `account.get_total_portfolio_value()`
- Get profit or loss: `account.get_profit_loss()`
- List holdings: `account.get_holdings()`
- List transactions: `account.get_transactions()`

This design encapsulates all the necessary components for the account management system, adhering to the requirements provided, and is structured in a way that can be easily tested and extended.