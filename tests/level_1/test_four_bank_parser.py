import datetime
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():

    cards = [
        BankCard(last_digits="1234", owner="Jane Smith"),
        BankCard(last_digits="5678", owner="John Doe"),
        BankCard(last_digits="9012", owner="Alice Johnson")
    ]

    sms_message = SmsMessage(
        text="1234567 89, 1234 01.04.23 15:30 Moscow some_details",
        author="John Doe",
        sent_at=datetime.datetime(2023, 4, 1)
    )

    result = parse_ineco_expense(sms=sms_message, cards=cards)

    assert result.amount == 1234567
    assert result.card == cards[0]
    assert result.spent_in == "Moscow some_details"
    assert result.spent_at == datetime.datetime(2023, 4, 1, 15, 30)

    