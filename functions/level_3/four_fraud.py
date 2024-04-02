from functions.level_3.models import Expense


def find_fraud_expenses(history: list[Expense]) -> list[Expense]:
    max_fraud_transaction_amount = 5000
    min_fraud_chain_length = 3

    expense_map = {}
    for expense in history:
        expense_key = expense.spent_in, expense.spent_at, expense.amount
        expense_map[expense_key] = expense_map.get(expense_key, 0) + 1

    fraud_signs = []
    for (spent_in, spent_at, amount), transactions_amount in expense_map.items():
        if (
            amount <= max_fraud_transaction_amount
            and transactions_amount >= min_fraud_chain_length
        ):
            fraud_signs.append((spent_in, spent_at, amount))

    fraud_transactions = []
    for spent_in, spent_at, amount in fraud_signs:
        fraud_transactions += [
            e
            for e in history
            if e.spent_in == spent_in and e.spent_at == spent_at and e.amount == amount
        ]
    return fraud_transactions
