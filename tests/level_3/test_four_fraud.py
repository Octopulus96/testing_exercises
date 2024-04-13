import decimal
import datetime
from typing import List
import pytest
from functions.level_3.models import Currency, ExpenseCategory, BankCard, Expense
from functions.level_3.four_fraud import find_fraud_expenses


@pytest.fixture
def variable_amount_expenses() -> List[Expense]:
    def factory(amounts: List[decimal.Decimal]) -> List[Expense]:
        return [
            Expense(
                amount=amount,
                currency=Currency.RUB,
                card=BankCard(last_digits="1234", owner="John Doe"),
                spent_in="SOMETHING",
                spent_at=datetime.datetime(2022, 1, 1),
                category=ExpenseCategory.BAR_RESTAURANT,
            )
            for amount in amounts
        ]

    return factory


@pytest.mark.parametrize(
    "amounts, expected",
    [
        (
            [
                decimal.Decimal("5000.00"),
                decimal.Decimal("5000.00"),
                decimal.Decimal("5000.00"),
            ],
            3,
        ),
        pytest.param(
            [
                decimal.Decimal("10000.00"),
                decimal.Decimal("10000.00"),
                decimal.Decimal("10000.00"),
            ],
            3,
            marks=pytest.mark.xfail(
                reason=(
                    "The condition 'if amount <= max_fraud_transaction_amount' ignores numbers above"
                    " 5000"
                ),
                run=True,
            ),
        ),
    ],
)
def test__find_fraud_expenses__suspicious_transactions_found_in_the_history(
    variable_amount_expenses: List[Expense], amounts: List[decimal.Decimal], expected: int
) -> None:
    assert len(find_fraud_expenses(variable_amount_expenses(amounts))) == expected


@pytest.mark.parametrize(
    "amounts, expected",
    [
        (
            [
                decimal.Decimal("100.00"),
                decimal.Decimal("5000.00"),
                decimal.Decimal("5000.00"),
            ],
            0,
        ),
        (
            [
                decimal.Decimal("100.00"),
                decimal.Decimal("10000.00"),
                decimal.Decimal("10000.00"),
            ],
            0,
        ),
    ],
)
def test__find_fraud_expenses__no_suspicious_transactions_were_found_in_the_history(
    variable_amount_expenses: List[Expense], amounts: List[decimal.Decimal], expected: int
) -> None:
    assert len(find_fraud_expenses(variable_amount_expenses(amounts))) == expected
