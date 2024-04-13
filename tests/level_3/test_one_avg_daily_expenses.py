import decimal
import datetime
from typing import List
import pytest
from functions.level_3.models import Currency, ExpenseCategory, BankCard, Expense
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


@pytest.fixture
def variable_amount_expenses() -> list[Expense]:
    def factory(amounts: list[decimal.Decimal]) -> list[Expense]:
        return [
            Expense(
                amount=amount,
                currency=Currency.RUB,
                card=BankCard(last_digits="1234", owner="John Doe"),
                spent_in="Bar Restaurant",
                spent_at=datetime.datetime.now() + datetime.timedelta(days=1),
                category=ExpenseCategory.BAR_RESTAURANT,
            )
            for amount in amounts
        ]

    return factory


@pytest.fixture()
def variable_spent_at_expenses() -> List[Expense]:
    def factory(dates: List[datetime.datetime]) -> List[Expense]:
        return [
            Expense(
                amount=decimal.Decimal("100.00"),
                currency=Currency.RUB,
                card=BankCard(last_digits="1234", owner="John Doe"),
                spent_in="Bar Restaurant",
                spent_at=date,
                category=ExpenseCategory.BAR_RESTAURANT,
            )
            for date in dates
        ]

    return factory


def test__calculate_average_daily_expenses__positive_amounts_counted(
    variable_amount_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_amount_expenses(
            [decimal.Decimal("100.00"), decimal.Decimal("200.00"), decimal.Decimal("300.00")]
        )
    ) == decimal.Decimal(600.00)


@pytest.mark.xfail(reason="Negative amounts are recognised in today's expenses", run=False)
def test__calculate_average_daily_expenses__zero_negative_does_not_count(
    variable_amount_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_amount_expenses(
            [decimal.Decimal("100.00"), decimal.Decimal("-100.00"), decimal.Decimal("-50.00")]
        )
    ) == decimal.Decimal(100.00)


def test__calculate_average_daily_expenses__zero_amounts_does_not_count(
    variable_amount_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_amount_expenses(
            [decimal.Decimal("100.00"), decimal.Decimal("0.00"), decimal.Decimal("0.00")]
        )
    ) == decimal.Decimal(100.00)


def test__calculate_average_daily_expenses__past_expenses_not_recognised(
    variable_spent_at_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_spent_at_expenses([
            datetime.datetime.now(),
            datetime.datetime.now() - datetime.timedelta(days=1),
            datetime.datetime.now() - datetime.timedelta(days=2),
        ])
    ) == decimal.Decimal(100.00)


def test__calculate_average_daily_expenses__future_expenses_not_recognised(
    variable_spent_at_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_spent_at_expenses([
            datetime.datetime.now(),
            datetime.datetime.now() + datetime.timedelta(days=1),
            datetime.datetime.now() + datetime.timedelta(days=2),
        ])
    ) == decimal.Decimal(100.00)


def test__calculate_average_daily_expenses__get_today_expenses(
    variable_spent_at_expenses: list[Expense],
) -> None:
    assert calculate_average_daily_expenses(
        variable_spent_at_expenses([
            datetime.datetime.now(),
            datetime.datetime.now(),
            datetime.datetime.now(),
        ])
    ) == decimal.Decimal(300.00)
