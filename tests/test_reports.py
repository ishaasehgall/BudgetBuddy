
import unittest
from features import reports


class TestAverageBalance(unittest.TestCase):
    def test_empty_history(self):
        self.assertEqual(reports.average_balance({"history": []}), 0.0)

    def test_multiple_balances(self):
        self.assertEqual(reports.average_balance({"history": [10, 20, 30]}), 20.0)
