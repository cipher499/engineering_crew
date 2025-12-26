class Account:
    def __init__(self, username: str, initial_deposit: float):
        """
        Initialize a new trading account.

        Parameters:
        username (str): The username for the account.
        initial_deposit (float): Initial amount of money deposited into the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.portfolio = {}  # A dictionary to hold stock symbols and their respective quantities
        self.transactions = []  # A list to keep track of transaction history
        self.initial_deposit = initial_deposit

    def deposit(self, amount: float):
        """
        Deposit funds into the account.

        Parameters:
        amount (float): Amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float):
        """
        Withdraw funds from the account.

        Parameters:
        amount (float): Amount to withdraw.

        Raises:
        ValueError: If the withdrawal would result in a negative balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")

    def buy_shares(self, stock_symbol: str, quantity: int, price_per_share: float):
        """
        Record the purchase of shares.

        Parameters:
        stock_symbol (str): The stock symbol to purchase.
        quantity (int): The number of shares to buy.
        price_per_share (float): The price of each share.

        Raises:
        ValueError: If the purchase exceeds available funds.
        """
        total_cost = quantity * price_per_share
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        
        self.balance -= total_cost
        if stock_symbol in self.portfolio:
            self.portfolio[stock_symbol] += quantity
        else:
            self.portfolio[stock_symbol] = quantity
        
        self.transactions.append(f"Bought {quantity} of {stock_symbol} at ${price_per_share:.2f} each")

    def sell_shares(self, stock_symbol: str, quantity: int, price_per_share: float):
        """
        Record the sale of shares.

        Parameters:
        stock_symbol (str): The stock symbol to sell.
        quantity (int): The number of shares to sell.
        price_per_share (float): The price of each share.

        Raises:
        ValueError: If attempting to sell more shares than owned.
        """
        if stock_symbol not in self.portfolio or self.portfolio[stock_symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        
        self.portfolio[stock_symbol] -= quantity
        total_revenue = quantity * price_per_share
        self.balance += total_revenue
        self.transactions.append(f"Sold {quantity} of {stock_symbol} at ${price_per_share:.2f} each")

    def get_portfolio_value(self, current_stock_prices: dict) -> float:
        """
        Calculate the total value of the user's portfolio.

        Parameters:
        current_stock_prices (dict): A dictionary mapping stock symbols to their current prices.

        Returns:
        float: The total value of the portfolio.
        """
        portfolio_value = self.balance
        for stock_symbol, quantity in self.portfolio.items():
            if stock_symbol in current_stock_prices:
                portfolio_value += quantity * current_stock_prices[stock_symbol]
        return portfolio_value

    def get_profit_loss(self) -> float:
        """
        Calculate the profit or loss from the initial deposit.

        Returns:
        float: The profit or loss.
        """
        total_value = self.get_portfolio_value({})
        return total_value - self.initial_deposit

    def get_holdings(self) -> dict:
        """
        Report the current holdings of the user.

        Returns:
        dict: A dictionary of stock symbols and their respective quantities.
        """
        return self.portfolio

    def get_profit_loss_report(self) -> float:
        """
        Report the profit or loss of the user.

        Returns:
        float: The total profit or loss.
        """
        return self.get_profit_loss()

    def get_transaction_history(self) -> list:
        """
        List the transactions made by the user over time.

        Returns:
        list: A list of transaction records.
        """
        return self.transactions