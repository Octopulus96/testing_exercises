import datetime
from typing import List
import pytest
from faker import Faker
from functions.level_1.four_bank_parser import (
    Expense,
    BankCard,
    SmsMessage,
    parse_ineco_expense,
)


@pytest.fixture(name="sms")
def fixture_sms(fake: Faker = Faker()) -> List[SmsMessage]:
    return [
        SmsMessage(
            text="1000 00, 0000 01.04.23 15:30 Moscow authcode 1234",
            author=fake.name(),
            sent_at=datetime.datetime(2023, 4, 1, 15, 30),
        ),
        SmsMessage(
            text="1111 00, 1111 01.04.23 15:30 Moscow authcode 1234",
            author=fake.name(),
            sent_at=datetime.datetime(2023, 4, 1, 15, 30),
        ),
    ]


@pytest.fixture(name="cards")
def fixture_cards() -> List[list[BankCard]]:
    return [
        [BankCard(last_digits="0000", owner="Иван Васильевич")],
        [BankCard(last_digits="1111", owner="Федор Достоевский")],
        [BankCard(last_digits="2222", owner="Лев Толстой")],
    ]


def test__parse_ineco_expense__conversion_of_datetime_to_str(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'spent_at' attribute of the summary is equal to the 'sent_at' attribute of the sms.
    """
    summary: Expense = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_at == sms[0].sent_at


def test__parse_ineco_expense__drop_amount_small_dignity(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'amount' attribute of the summary is equal to 1000 if the amount in the sms is smaller than 1000.
    """
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.amount == 1000


def test__parse_ineco_expense__card_is_not_added_to_the_List(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that an IndexError is raised when the List of cards does not contain the card used in the sms.
    """
    with pytest.raises(IndexError):
        summary: Expense = parse_ineco_expense(sms[0], cards[2])


def test__parse_ineco_expense__extracting_card_from_empty_List_causes_IndexError(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that an IndexError is raised when the List of cards is empty.
    """
    with pytest.raises(IndexError):
        parse_ineco_expense(sms[0], [])


def test__parse_ineco_expense__get_location_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'spent_in' attribute of the summary is equal to the author of the sms.
    """
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_in == "Moscow"


def test__parse_ineco_expense__received_location_from_sms_does_not_match(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'spent_in' attribute of the summary is not equal to the author of the sms if the author is from a different city.
    """
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_in != "Paris"


def test__parse_ineco_expense__get_BankCard_by_4_digits_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'card' attribute of the summary is equal to the first card in the List that matches the last 4 digits of the card in the sms.
    """
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.card.last_digits == cards[0][0].last_digits


def test__parse_ineco_expense__BankCard_by_the_last_4_digits_card_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    """
    Test that the 'card' attribute of the summary is equal to the first card in the List that matches the last 4 digits of the card in the sms.
    """
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.card.last_digits == cards[0][0].last_digits
