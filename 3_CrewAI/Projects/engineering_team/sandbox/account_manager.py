import datetime

class Transaction:
    def __init__(self, transaction_type, symbol, quantity, price_per_share):
        self.type = transaction_type  # either 'buy' or 'sell'
        self.symbol = symbol
        self.quantity = quantity
        self.price_per_share = price_per_share
        self.timestamp = datetime.datetime.now().isoformat()

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, initial_deposit):
        if username in self.accounts:
            return False
        self.accounts[username] = {
            'balance': initial_deposit,
            'holdings': {},
            'transactions': [],
            'initial_deposit': initial_deposit
        }
        return True

    def deposit(self, username, amount):
        if username not in self.accounts:
            return False
        self.accounts[username]['balance'] += amount
        return True

    def withdraw(self, username, amount):
        if username not in self.accounts:
            return False
        current_balance = self.accounts[username]['balance']
        if self.prevent_negative_balance(current_balance, amount):
            self.accounts[username]['balance'] -= amount
            return True
        return False

    def buy_shares(self, username, symbol, quantity):
        if username not in self.accounts:
            return False
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity

        if self.prevent_overbuy(self.accounts[username]['balance'], share_price, quantity):
            self.accounts[username]['balance'] -= total_cost
            self.accounts[username]['transactions'].append(
                Transaction('buy', symbol, quantity, share_price)
            )
            if symbol in self.accounts[username]['holdings']:
                self.accounts[username]['holdings'][symbol] += quantity
            else:
                self.accounts[username]['holdings'][symbol] = quantity
            return True
        return False  # No balance change if buy fails

    def sell_shares(self, username, symbol, quantity):
        if username not in self.accounts:
            return False
        if symbol in self.accounts[username]['holdings']:
            if self.prevent_over_sell(self.accounts[username]['holdings'], symbol, quantity):
                share_price = get_share_price(symbol)
                self.accounts[username]['holdings'][symbol] -= quantity
                if self.accounts[username]['holdings'][symbol] == 0:
                    del self.accounts[username]['holdings'][symbol]
                self.accounts[username]['balance'] += share_price * quantity
                self.accounts[username]['transactions'].append(
                    Transaction('sell', symbol, quantity, share_price)
                )
                return True
        return False

    def get_portfolio_value(self, username):
        if username not in self.accounts:
            return 0.0
        total_value = self.accounts[username]['balance']
        for symbol, quantity in self.accounts[username]['holdings'].items():
            total_value += quantity * get_share_price(symbol)
        return total_value

    def get_profit_loss(self, username):
        if username not in self.accounts:
            return 0.0
        current_value = self.get_portfolio_value(username)
        return current_value - self.accounts[username]['initial_deposit']

    def get_holdings(self, username):
        if username not in self.accounts:
            return {}
        return self.accounts[username]['holdings']

    def get_transactions(self, username):
        if username not in self.accounts:
            return []
        return self.accounts[username]['transactions']

    # Helper functions to check for constraints
    def prevent_negative_balance(self, current_balance, withdrawal_amount):
        return current_balance >= withdrawal_amount

    def prevent_overbuy(self, current_balance, share_price, quantity):
        return current_balance >= share_price * quantity

    def prevent_over_sell(self, user_holdings, symbol, quantity):
        return user_holdings.get(symbol, 0) >= quantity


def get_share_price(symbol):
    # Fixed share prices for simulation
    prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)