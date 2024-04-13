import decimal
import datetime
from typing import List
import pytest
from functions.level_3.models import Currency, ExpenseCategory, BankCard, Expense
from functions.level_3.three_is_subscription import is_subscription


@pytest.fixture(name="expenses_by_date_and_time")
def fixture_expenses_by_date_and_time(expense_by_date_and_time: Expense) -> List[Expense]:
    def factory_expenses(
        spent_in_list: List[str], spent_at_list: List[datetime.datetime]
    ) -> List[Expense]:
        return [
            expense_by_date_and_time(spent_in, spent_at)
            for spent_in, spent_at in zip(spent_in_list, spent_at_list)
        ]

    return factory_expenses


@pytest.fixture(name="expense_by_date_and_time")
def fixture_expense_by_date_and_time() -> Expense:
    def factory_expense(spent_in: str, spent_at: datetime.datetime) -> Expense:
        return Expense(
            amount=decimal.Decimal("100.00"),
            currency=Currency.RUB,
            card=BankCard(last_digits="1234", owner="John Doe"),
            spent_in=spent_in,
            spent_at=spent_at,
            category=ExpenseCategory.BAR_RESTAURANT,
        )

    return factory_expense


def test__is_subscription__transactions_repeated_3_months_in_arow_is_subscription(
    expenses_by_date_and_time: List[Expense], expense_by_date_and_time: Expense
) -> None:
    history = expenses_by_date_and_time(
        ["Amazon", "Amazon", "Amazon", "Netflix"],
        [
            datetime.datetime(2022, 1, 1),
            datetime.datetime(2022, 2, 1),
            datetime.datetime(2022, 3, 1),
            datetime.datetime(2022, 4, 1),
        ],
    )
    expense = expense_by_date_and_time("Amazon", datetime.datetime(2022, 1, 1))
    assert is_subscription(expense=expense, history=history) is True


def test__is_subscription__transactions_recurring_for_less_than_3_months_are_not_a_subscription(
    expenses_by_date_and_time: List[Expense], expense_by_date_and_time: Expense
) -> None:
    history = expenses_by_date_and_time(
        ["Amazon", "Amazon", "Amazon", "Netflix", "Netflix"],
        [
            datetime.datetime(2022, 1, 1),
            datetime.datetime(2022, 2, 1),
            datetime.datetime(2022, 3, 1),
            datetime.datetime(2022, 4, 1),
            datetime.datetime(2022, 5, 1),
        ],
    )
    expense = expense_by_date_and_time("Netflix", datetime.datetime(2022, 5, 1))
    assert is_subscription(expense=expense, history=history) is False
