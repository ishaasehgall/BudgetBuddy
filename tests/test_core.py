
"""Example tests for BudgetBuddy."""

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_balance(self):
        data = {"starting_balance": 50.0, "transactions": [
            {"id": 1, "description": "Bus pass", "amount": -2.5, "category": "transport"},
            {"id": 2, "description": "Allowance", "amount": 20.0, "category": "income"},
        ]}
        self.assertEqual(core.balance(data), 67.5)

    def test_add_transaction_gives_a_new_id(self):
        data = {"transactions": [{"id": 1, "description": "t", "amount": 5.0, "category": "general"}]}
        tx = core.add_transaction(data, "New thing", -3.0)
        self.assertEqual(tx["id"], 2)
        self.assertEqual(len(data["transactions"]), 2)

    def test_big_expenses_mixed_transactions(self):
        transactions = [
            {"id": 1, "description": "Lunch", "amount": -8.0, "category": "food"},
            {"id": 2, "description": "Shoes", "amount": -45.0, "category": "shopping"},
            {"id": 3, "description": "Allowance", "amount": 50.0, "category": "income"},
            {"id": 4, "description": "Movie", "amount": -10.0, "category": "entertainment"},
        ]

        result = core.big_expenses(transactions, 10)

        self.assertEqual(
            [t["description"] for t in result],
            ["Shoes", "Movie"]
        )

    def test_big_expenses_nothing_qualifies(self):
        transactions = [
            {"id": 1, "description": "Lunch", "amount": -5.0, "category": "food"},
            {"id": 2, "description": "Allowance", "amount": 50.0, "category": "income"},
        ]

        result = core.big_expenses(transactions, 10)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
