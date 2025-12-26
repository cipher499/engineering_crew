from accounts import Account
import gradio as gr

# Create a simple instance of an Account
username = "User1"
initial_deposit = 1000.0
account = Account(username, initial_deposit)

def create_account(initial_deposit):
    global account
    account = Account(username, initial_deposit)
    return f"Account created for {username} with initial deposit of ${initial_deposit:.2f}"

def deposit_funds(amount):
    try:
        account.deposit(amount)
        return f"Deposited: ${amount:.2f}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: ${amount:.2f}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def buy_shares(stock_symbol, quantity, price_per_share):
    try:
        account.buy_shares(stock_symbol, quantity, price_per_share)
        return f"Bought {quantity} of {stock_symbol} at ${price_per_share:.2f} each."
    except ValueError as e:
        return str(e)

def sell_shares(stock_symbol, quantity, price_per_share):
    try:
        account.sell_shares(stock_symbol, quantity, price_per_share)
        return f"Sold {quantity} of {stock_symbol} at ${price_per_share:.2f} each."
    except ValueError as e:
        return str(e)

def get_portfolio_value(current_stock_prices):
    current_stock_prices_dict = eval(current_stock_prices)  # Convert string input to dict
    value = account.get_portfolio_value(current_stock_prices_dict)
    return f"Total value of portfolio: ${value:.2f}"

def get_profit_loss():
    profit_loss = account.get_profit_loss()
    return f"Profit/Loss: ${profit_loss:.2f}"

def get_holdings():
    holdings = account.get_holdings()
    return f"Current holdings: {holdings}"

def get_transaction_history():
    transactions = account.get_transaction_history()
    return f"Transaction history: {transactions}"

with gr.Blocks() as demo:
    gr.Markdown("# Trading Account Management System")
    
    with gr.Box():
        gr.Markdown("## Create Account")
        initial_deposit_input = gr.Number(label="Initial Deposit", value=1000.0)
        create_account_button = gr.Button("Create Account")
        create_account_output = gr.Output()
        create_account_button.click(create_account, inputs=initial_deposit_input, outputs=create_account_output)

    with gr.Box():
        gr.Markdown("## Deposit Funds")
        deposit_input = gr.Number(label="Amount to Deposit", value=100.0)
        deposit_button = gr.Button("Deposit")
        deposit_output = gr.Output()
        deposit_button.click(deposit_funds, inputs=deposit_input, outputs=deposit_output)
    
    with gr.Box():
        gr.Markdown("## Withdraw Funds")
        withdraw_input = gr.Number(label="Amount to Withdraw", value=100.0)
        withdraw_button = gr.Button("Withdraw")
        withdraw_output = gr.Output()
        withdraw_button.click(withdraw_funds, inputs=withdraw_input, outputs=withdraw_output)

    with gr.Box():
        gr.Markdown("## Buy Shares")
        stock_symbol_input_buy = gr.Textbox(label="Stock Symbol")
        quantity_input_buy = gr.Number(label="Quantity", value=1)
        price_per_share_input_buy = gr.Number(label="Price Per Share", value=10.0)
        buy_button = gr.Button("Buy Shares")
        buy_output = gr.Output()
        buy_button.click(buy_shares, inputs=[stock_symbol_input_buy, quantity_input_buy, price_per_share_input_buy], outputs=buy_output)

    with gr.Box():
        gr.Markdown("## Sell Shares")
        stock_symbol_input_sell = gr.Textbox(label="Stock Symbol")
        quantity_input_sell = gr.Number(label="Quantity", value=1)
        price_per_share_input_sell = gr.Number(label="Price Per Share", value=10.0)
        sell_button = gr.Button("Sell Shares")
        sell_output = gr.Output()
        sell_button.click(sell_shares, inputs=[stock_symbol_input_sell, quantity_input_sell, price_per_share_input_sell], outputs=sell_output)

    with gr.Box():
        gr.Markdown("## Get Portfolio Value")
        current_stock_prices_input = gr.Textbox(label="Current Stock Prices (e.g., {'AAPL': 150.0, 'GOOGL': 2800.0})")
        portfolio_value_button = gr.Button("Get Portfolio Value")
        portfolio_value_output = gr.Output()
        portfolio_value_button.click(get_portfolio_value, inputs=current_stock_prices_input, outputs=portfolio_value_output)

    with gr.Box():
        gr.Markdown("## Get Profit/Loss")
        profit_loss_button = gr.Button("Get Profit/Loss")
        profit_loss_output = gr.Output()
        profit_loss_button.click(get_profit_loss, outputs=profit_loss_output)

    with gr.Box():
        gr.Markdown("## Get Holdings")
        holdings_button = gr.Button("Get Holdings")
        holdings_output = gr.Output()
        holdings_button.click(get_holdings, outputs=holdings_output)

    with gr.Box():
        gr.Markdown("## Get Transaction History")
        transaction_history_button = gr.Button("Get Transaction History")
        transaction_history_output = gr.Output()
        transaction_history_button.click(get_transaction_history, outputs=transaction_history_output)

demo.launch()