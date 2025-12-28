import gradio as gr
from accounts import Account

account = Account('user123', 1000.0)

def deposit(amount):
    try:
        account.deposit(amount)
        return f"Deposited: ${amount}. Current balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def withdraw(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: ${amount}. Current balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def buy_stock(symbol, quantity):
    try:
        account.buy_stock(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}. Current balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def sell_stock(symbol, quantity):
    try:
        account.sell_stock(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}. Current balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def show_portfolio():
    total_value = account.get_total_portfolio_value()
    return f"Total Portfolio Value: ${total_value}. Holdings: {account.get_holdings()}."

def show_profit_loss():
    profit_loss = account.get_profit_loss()
    return f"Profit/Loss: ${profit_loss}."

def show_transactions():
    transactions = account.get_transactions()
    return f"Transactions: {transactions}."

with gr.Blocks() as app:
    gr.Markdown("## Account Management System")
    
    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Output", interactive=False)

    deposit_button.click(fn=deposit, inputs=deposit_amount, outputs=deposit_output)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Output", interactive=False)

    withdraw_button.click(fn=withdraw, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Row():
        buy_symbol = gr.Textbox(label="Buy Symbol (AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy Stock")
        buy_output = gr.Textbox(label="Output", interactive=False)

    buy_button.click(fn=buy_stock, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Row():
        sell_symbol = gr.Textbox(label="Sell Symbol (AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Quantity")
        sell_button = gr.Button("Sell Stock")
        sell_output = gr.Textbox(label="Output", interactive=False)

    sell_button.click(fn=sell_stock, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Row():
        portfolio_button = gr.Button("Show Portfolio Value")
        portfolio_output = gr.Textbox(label="Output", interactive=False)

    portfolio_button.click(fn=show_portfolio, outputs=portfolio_output)

    with gr.Row():
        profit_loss_button = gr.Button("Show Profit/Loss")
        profit_loss_output = gr.Textbox(label="Output", interactive=False)

    profit_loss_button.click(fn=show_profit_loss, outputs=profit_loss_output)

    with gr.Row():
        transactions_button = gr.Button("Show Transactions")
        transactions_output = gr.Textbox(label="Output", interactive=False)

    transactions_button.click(fn=show_transactions, outputs=transactions_output)

app.launch()