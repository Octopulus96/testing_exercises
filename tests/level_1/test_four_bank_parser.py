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

# Полностью переписать, из-за [0] в тестах не понятно какие данные принимает на вход, особенно cards[0][0].last_digits
#
# Вместо статичных фикстур, лучше сделать фикстуры фабрики, которые будут друг на друга работать
# 1. Фикстура фабрика для создания одного экземпляра BankCard, потом её передаим в другую фабрику,
# где уже можно будет генерировать любое колличество с любыми параметрами
# 2. Фабрика смс, принимает результат фабрики текста, желательно бы ещё добавить возможновть изменять
# время получения в SmsMessage и в тексте, для этого можно добавить ещё фабрику для преобразования
# текста в datime
# Фабрика с текстом смс, нам важна связка номера карты в тексте и в BankCard,
# можно передавать одиночный экземпляр BankCard сгенерированый фабрикой карт


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
    summary: Expense = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_at == sms[0].sent_at


def test__parse_ineco_expense__drop_amount_small_dignity(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.amount == 1000


def test__parse_ineco_expense__card_is_not_added_to_the_List(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    with pytest.raises(IndexError):
        summary: Expense = parse_ineco_expense(sms[0], cards[2])


def test__parse_ineco_expense__extracting_card_from_empty_List_causes_IndexError(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    with pytest.raises(IndexError):
        parse_ineco_expense(sms[0], [])


def test__parse_ineco_expense__get_location_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_in == "Moscow"


def test__parse_ineco_expense__received_location_from_sms_does_not_match(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.spent_in != "Paris"


def test__parse_ineco_expense__get_BankCard_by_4_digits_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.card.last_digits == cards[0][0].last_digits


def test__parse_ineco_expense__BankCard_by_the_last_4_digits_card_from_sms(
    sms: List[SmsMessage], cards: List[list[BankCard]]
) -> None:
    summary = parse_ineco_expense(sms[0], cards[0])
    assert summary.card.last_digits == cards[0][0].last_digits
