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

def test__parse_ineco_expense__amount_method_returns_the_transaction_amount_from_sms_cutting_off_the_small_dignity(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.amount == 1234567

def test__parse_ineco_expense__card_method_finds_the_last_4_digits_of_the_card_from_the_sms_in_the_list_of_existing_cards(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.card == sample_cards[0]

def test__parse_ineco_expense__spent_in_method_returns_additional_information_from_the_end_of_the_sms(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards)
    assert summary.spent_in == "Moscow some_details"

def test__parse_ineco_expense__method_spent_at_gets_date_from_sms_and_converts_it_to_datetime(sample_sms_message, sample_cards):
    summary = parse_ineco_expense(sms=sample_sms_message[0], cards=sample_cards) 
    assert summary.spent_at == datetime.datetime(2023, 4, 1, 15, 30)

    