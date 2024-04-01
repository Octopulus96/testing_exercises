import datetime, pytest
from faker import Faker
from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense

NOT_SET = "___"

@pytest.fixture
def make_sms(fake=Faker()):
    def inner(text: str = NOT_SET, author: str = NOT_SET, sent_at: datetime.datetime = NOT_SET):
        return SmsMessage(
            text = '1000 00, 1234567812345678 20.04.2024 15:30 Congo authcode 1234' if text is NOT_SET else text, 
            author=fake.company() if author is NOT_SET else author, 
            sent_at=fake.date_time_between(start_date=datetime.datetime(2023, 1, 1, 00, 00)) if sent_at is NOT_SET else sent_at
        )
    return inner
    

@pytest.fixture
def make_sms_text(fake=Faker()):
    def inner(amount: str = NOT_SET, spent_at: datetime.datetime = NOT_SET, last_digits: str = NOT_SET, city: str = NOT_SET):
        date_time_str_patern = '%d.%m.%y %H:%M'
        dignity = fake.random_number(digits=None, fix_len=False)
        small_dignity = fake.random_number(digits=2, fix_len=True)
        city = fake.city() if city is NOT_SET else city
        amount = f"{dignity} {small_dignity}" if amount is NOT_SET else amount
        spent_at = fake.date_time_between(start_date=datetime.datetime(2023, 1, 1, 00, 00)) if spent_at is NOT_SET else spent_at
        last_digits = fake.random_number(digits=16, fix_len=True) if last_digits is NOT_SET else last_digits
        return f"{amount}, {last_digits} {spent_at.strftime(date_time_str_patern)} {city} authcode 1234"
    return inner


@pytest.fixture
def make_cards(fake=Faker()):
    def inner(last_digits: str = NOT_SET, owner: str = NOT_SET):
        return [
            BankCard(
                last_digits=str(fake.random_number(digits=4, fix_len=True)) if last_digits is NOT_SET else last_digits,
                owner=fake.name() if owner is NOT_SET else owner)
        ]
    return inner


def test__parse_ineco_expense__conversion_of_datetime_to_str(make_sms, make_sms_text, make_cards):
    date_time = datetime.datetime(2023, 4, 1, 15, 30)
    cards = make_cards()
    sms_text = make_sms_text(spent_at=date_time, last_digits=cards[0].last_digits)
    summary = parse_ineco_expense(make_sms(text=sms_text, sent_at=date_time), cards)
    assert summary.spent_at == date_time


def test__parse_ineco_expense__drop_amount_small_dignity(make_sms, make_sms_text, make_cards):
    full_amount = "1010 10"
    cards = make_cards()
    sms_text = make_sms_text(amount=full_amount, last_digits=cards[0].last_digits)
    summary = parse_ineco_expense(make_sms(text=sms_text), cards)
    assert summary.amount == 1010


@pytest.mark.xfail(reason="When calling bank_cards fixture, I encountered IndexError if I don't force last_digits to be a str", run=True)
def test__parse_ineco_expense__card_is_not_added_to_the_list(make_sms, make_sms_text, make_cards):
    cards = make_cards(last_digits=int(1234), owner="SomeName")
    sms_text = make_sms_text(last_digits=cards[0].last_digits)
    with pytest.raises(IndexError):
        summary = parse_ineco_expense(make_sms(text=sms_text), cards)
        assert summary.card == cards[0]


@pytest.mark.xfail(reason="No processing in case of an attempt to get an object from an empty list", run=True)
def test__parse_ineco_expense__extracting_card_from_empty_list_causes_IndexError(make_sms):
    cards = []
    with pytest.raises(IndexError):
        summary = parse_ineco_expense(make_sms(), cards)


def test__parse_ineco_expense__get_BankCard_by_the_last_4_digits_card_from_sms(make_sms, make_sms_text, make_cards):
    cards = make_cards(last_digits="1234")
    sms_text = make_sms_text(last_digits="9876123498761234")
    summary = parse_ineco_expense(make_sms(text=sms_text), cards)
    assert summary.card == cards[0]


def test__parse_ineco_expense__get_BankCard_by_4_digits_from_sms(make_sms, make_sms_text, make_cards):
    cards = make_cards(last_digits="1234")
    sms_text = make_sms_text(last_digits="1234")
    summary = parse_ineco_expense(make_sms(text=sms_text), cards)
    assert summary.card == cards[0]


def test__parse_ineco_expense__get_transaction_location_from_sms(make_sms, make_sms_text, make_cards):
    cards = make_cards()
    sms_text = make_sms_text(city="Moscow", last_digits=cards[0].last_digits)
    summary = parse_ineco_expense(make_sms(text=sms_text), cards)
    assert summary.spent_in == "Moscow"

def test__parse_ineco_expense__received_transaction_location_from_sms_does_not_match(make_sms, make_sms_text, make_cards):
    cards = make_cards()
    sms_text = make_sms_text(city="Moscow", last_digits=cards[0].last_digits)
    summary = parse_ineco_expense(make_sms(text=sms_text), cards)
    assert summary.spent_in != "Monako"
