"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    report = {}

    for transaction in data["transactions"]:
        category = transaction["category"]
        amount = transaction["amount"]

        if category not in report:
            report[category] = 0

        report[category] += amount

    return report
