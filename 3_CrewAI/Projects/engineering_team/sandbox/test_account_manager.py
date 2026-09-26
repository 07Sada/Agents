import unittest
from account_manager import AccountManager, get_share_price

class TestAccountManager(unittest.TestCase):

    def setUp(self):
        self.manager = AccountManager()
        self.manager.create_account('test_user', 1000.0)

    def test_create_account(self):
        self.assertTrue(self.manager.create_account('new_user', 500.0))
        self.assertFalse(self.manager.create_account('test_user', 200.0))

    def test_deposit(self):
        self.manager.deposit('test_user', 200.0)
        self.assertEqual(self.manager.accounts['test_user']['balance'], 1200.0)

    def test_withdraw_with_sufficient_balance(self):
        self.manager.withdraw('test_user', 200.0)
        self.assertEqual(self.manager.accounts['test_user']['balance'], 800.0)

    def test_withdraw_insufficient_balance(self):
        self.assertFalse(self.manager.withdraw('test_user', 2000.0))
        self.assertEqual(self.manager.accounts['test_user']['balance'], 1000.0)

    def test_buy_shares_with_sufficient_funds(self):
        self.assertTrue(self.manager.buy_shares('test_user', 'AAPL', 2))
        self.assertEqual(self.manager.accounts['test_user']['balance'], 700.0)
        self.assertEqual(self.manager.accounts['test_user']['holdings']['AAPL'], 2)

    def test_buy_shares_without_sufficient_funds(self):
        self.assertFalse(self.manager.buy_shares('test_user', 'AAPL', 10))
        self.assertEqual(self.manager.accounts['test_user']['balance'], 700.0)

    def test_sell_shares_with_sufficient_holdings(self):
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.assertTrue(self.manager.sell_shares('test_user', 'AAPL', 1))
        self.assertEqual(self.manager.accounts['test_user']['holdings']['AAPL'], 1)
        self.assertEqual(self.manager.accounts['test_user']['balance'], 850.0)

    def test_sell_shares_insufficient_holdings(self):
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.assertFalse(self.manager.sell_shares('test_user', 'AAPL', 3))
        self.assertEqual(self.manager.accounts['test_user']['holdings']['AAPL'], 2)

    def test_get_portfolio_value(self):
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.assertAlmostEqual(self.manager.get_portfolio_value('test_user'), 700.0 + (150.0 * 2))

    def test_get_profit_loss(self):
        self.assertAlmostEqual(self.manager.get_profit_loss('test_user'), -1000.0)
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.assertAlmostEqual(self.manager.get_profit_loss('test_user'), -1000.0 + (150.0 * 2))

    def test_get_holdings(self):
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.assertEqual(self.manager.get_holdings('test_user'), {'AAPL': 2})

    def test_get_transactions(self):
        self.manager.buy_shares('test_user', 'AAPL', 2)
        self.manager.sell_shares('test_user', 'AAPL', 1)
        transactions = self.manager.get_transactions('test_user')
        self.assertEqual(len(transactions), 2)

if __name__ == '__main__':
    unittest.main()