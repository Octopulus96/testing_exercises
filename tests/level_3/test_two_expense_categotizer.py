import datetime
import decimal
import pytest
from functions.level_3.models import Currency, ExpenseCategory, BankCard, Expense
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger


@pytest.fixture
def variable_spent_in_expenses() -> Expense:
    def factory(spent_in: str) -> Expense:
        return Expense(
            amount=decimal.Decimal("100.00"),
            currency=Currency.RUB,
            card=BankCard(last_digits="1234", owner="John Doe"),
            spent_in=spent_in,
            spent_at=datetime.datetime.now(),
            category=ExpenseCategory.BAR_RESTAURANT,
        )

    return factory


@pytest.fixture(params=[" ", ",", ".", "-", "/", "\\"])
def different_punctuation_string(request: pytest.FixtureRequest) -> str:
    return f"asador{request.param}julis{request.param}doc{request.param}set{request.param}bastard"


@pytest.mark.parametrize(
    "possible_category, triggers",
    [
        (ExpenseCategory.BAR_RESTAURANT, "asador,julis,doc,set,bastard"),
        (ExpenseCategory.SUPERMARKET, "chinar,sas,green apple,meat house,clean house"),
        (ExpenseCategory.ONLINE_SUBSCRIPTIONS, "apple.com/bill,leetcode.com,zoom.us,netflix"),
        (ExpenseCategory.MEDICINE_PHARMACY, "farm,pharm,alfa-pharm,maname"),
        (ExpenseCategory.THEATRES_MOVIES_CULTURE, "tomsarkgh,moscow cinema,kino park,cinema galleria"),
        (ExpenseCategory.TRANSPORT, "gg platform,www.taxi.yandex.ru,bolt.eu,yandex go"),
    ],
)
def test__guess_expense_category__trigger_is_activated_get_the_category(
    possible_category: ExpenseCategory, triggers: str, variable_spent_in_expenses: Expense
) -> None:
    expense = variable_spent_in_expenses(triggers)
    assert guess_expense_category(expense=expense) == possible_category


def test__guess_expense_category__trigger_does_not_fit_any_category(
    variable_spent_in_expenses: Expense,
) -> None:
    expense = variable_spent_in_expenses("stone island")
    assert guess_expense_category(expense) is None


def test__is_string_contains_trigger__allowed_punktuation_formats(
    different_punctuation_string: str,
) -> None:
    assert is_string_contains_trigger(different_punctuation_string, "asador") is True


@pytest.mark.parametrize(
    "original_string, trigger, expected",
    [
        pytest.param(
            "asador,sas,green apple,meat house,clean house",
            "asador",
            True,
            id="trigger_at_the_beginning",
        ),
        pytest.param(
            "chinar,sas,green apple,asador,meat house,clean house",
            "asador",
            True,
            id="triger_in_the_middle",
        ),
        pytest.param(
            "chinar,sas,green apple,meat house,asador", "asador", True, id="triger_is_at_the_end"
        ),
    ],
)
def test__is_string_contains_trigger__trigger_is_at_beginning_middle_end_of_the_string(
    original_string: str, trigger: str, expected: bool
) -> None:
    assert is_string_contains_trigger(original_string, trigger) == expected


def test__is_string_contains_trigger__trigger_not_found_in_string() -> None:
    assert is_string_contains_trigger("camel,adidas,stone island", "leetcode.com") is False
