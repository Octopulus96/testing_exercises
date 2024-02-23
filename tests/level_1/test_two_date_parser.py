import datetime
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    assert compose_datetime_from("today", "12:00") == datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
    assert compose_datetime_from("tomorrow", "12:00") == (datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=12, minute=0, second=0, microsecond=0)