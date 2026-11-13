import unittest
from features import reports


class TestCategoryReport(unittest.TestCase):

    def test_category_totals(self):
        data = {
            "transactions": [
                {"category": "food", "amount": -10},
                {"category": "fun", "amount": -20},
                {"category": "food", "amount": -5},
                {"category": "income", "amount": 50}
            ]
        }

        expected = {
            "food": -15,
            "fun": -20,
            "income": 50
        }

        self.assertEqual(reports.category_report(data), expected)

    def test_empty_transactions(self):
        data = {"transactions": []}
        self.assertEqual(reports.category_report(data), {})


if __name__ == "__main__":
    unittest.main()