import gradio as gr
from account_manager import AccountManager, get_share_price

# Initialize the Account Manager
manager = AccountManager()

# Function to create an account
def create_account(username, initial_deposit):
    if manager.create_account(username, initial_deposit):
        return f"Account '{username}' created with initial deposit {initial_deposit}"
    return "Account creation failed: Account already exists."

# Function to deposit funds
def deposit_funds(username, amount):
    if manager.deposit(username, amount):
        return f"Deposited {amount}. New balance: {manager.accounts[username]['balance']}"
    return "Deposit failed: Account not found."

# Function to withdraw funds
def withdraw_funds(username, amount):
    if manager.withdraw(username, amount):
        return f"Withdrew {amount}. New balance: {manager.accounts[username]['balance']}"
    return "Withdrawal failed: Insufficient balance or account not found."

# Function to buy shares
def buy_shares(username, symbol, quantity):
    if manager.buy_shares(username, symbol, quantity):
        return f"Bought {quantity} shares of {symbol}."
    return "Buy failed: Insufficient funds or account not found."

# Function to sell shares
def sell_shares(username, symbol, quantity):
    if manager.sell_shares(username, symbol, quantity):
        return f"Sold {quantity} shares of {symbol}."
    return "Sell failed: Insufficient shares or account not found."

# Functions to display various information
def display_info(func_name, username, amount=None, symbol=None, quantity=None):
    if func_name == 'Create Account':
        return create_account(username, amount)
    elif func_name == 'Deposit':
        return deposit_funds(username, amount)
    elif func_name == 'Withdraw':
        return withdraw_funds(username, amount)
    elif func_name == 'Buy Shares':
        return buy_shares(username, symbol, quantity)
    elif func_name == 'Sell Shares':
        return sell_shares(username, symbol, quantity)
    elif func_name == 'Show Portfolio Value':
        return display_portfolio_value(username)
    elif func_name == 'Show Profit/Loss':
        return display_profit_loss(username)
    elif func_name == 'Show Holdings':
        return display_holdings(username)
    elif func_name == 'Show Transactions':
        return display_transactions(username)

# Gradio Interface
app = gr.Interface(
    fn=display_info,
    inputs=[
        gr.Dropdown(label="Action", choices=["Create Account", "Deposit", "Withdraw", "Buy Shares", "Sell Shares", "Show Portfolio Value", "Show Profit/Loss", "Show Holdings", "Show Transactions"]),
        gr.Textbox(label="Username"),
        gr.Number(label="Initial Deposit"),
        gr.Textbox(label="Share Symbol"),
        gr.Number(label="Quantity")
    ],
    outputs="text"
)

if __name__ == "__main__":
    app.launch()