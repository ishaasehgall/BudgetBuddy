
# BudgetBuddy

BudgetBuddy is a Python spending and allowance tracker that helps users keep track of their transactions, check their balance, and understand their spending.

## Features

- View your current account balance
- Add and save transactions
- View your transaction history
- Filter transactions by category
- View your most recent transaction
- See how many transactions belong to each category
- View total spending and average transaction amounts
- View a basic account summary

## How to Run

1. Open the project in VS Code or GitHub Codespaces.
2. Open the terminal.
3. Run:

```bash
python main.py
```

4. Enter a number from the menu to use a feature.

## Run Tests

```bash
python -m unittest
```

## Project Structure

- `main.py` - Main menu and user interaction
- `storage.py` - Loads and saves transaction data
- `features/core.py` - Transaction and balance functions
- `features/reports.py` - Account summary and reporting functions
- `data/budgetbuddy.json` - Stored transaction data
- `tests/` - Unit tests

## Known Limitations

- BudgetBuddy currently runs in the terminal.
- The category totals report is still under development.
- Transactions added through the menu use the default category.
- Some features may not handle empty transaction histories.

## Developer

Isha Sehgal - Solo Developer

Built as part of Code2College Elite 101.
