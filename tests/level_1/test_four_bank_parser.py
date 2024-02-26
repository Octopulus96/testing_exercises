import datetime, pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

@pytest.fixture
def sample_cards():
    return [
        BankCard(last_digits="1234", owner="Jane Smith"),
        BankCard(last_digits="5678", owner="John Doe"),
        BankCard(last_digits="9012", owner="Alice Johnson")
    ]

@pytest.fixture
def sample_sms_message():
    return [
        SmsMessage(
        text="1234567 89, 1234 01.04.23 15:30 Moscow some_details",
        author="BANK OF AMERICA",
        sent_at=datetime.datetime(2023, 4, 1)
        ),
        SmsMessage(
        text="32500 00, 5678 23.02.24 23:17 Los Angeles some_details",
        author="BANK OF AMERICA",
        sent_at=datetime.datetime(2024, 2, 23)
        ),
        SmsMessage(
        text="1000000 00, 9012 25.06.22 11:10 Bali some_details",
        author="BANK OF AMERICA",
        sent_at=datetime.datetime(2022, 6, 25)
        )
    ]

def test_parse_ineco_expense_amount(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.amount == 1234567

def test_parse_ineco_expense_card(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.card == sample_cards[0]

def test_parse_ineco_expense_spent_in(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.spent_in == "Moscow some_details"

def test_parse_ineco_expense_spent_at(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards) 
    assert summary.spent_at == datetime.datetime(2023, 4, 1, 15, 30)

    