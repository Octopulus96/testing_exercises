import datetime
from freezegun import freeze_time

from functions.level_1.two_date_parser import compose_datetime_from

@freeze_time("2024-02-23 12:00:00")
def test_compose_datetime_from_today_12_00():
    assert compose_datetime_from("today", "12:00") == datetime.datetime.now()

@freeze_time("2024-02-23 12:00:00")
def test_compose_datetime_from_tomorrow_12_00():
    assert compose_datetime_from("tomorrow", "12:00") == datetime.datetime.now() + datetime.timedelta(days=1)

@freeze_time("2024-02-23 21:30:00")
def test_compose_datetime_from_today_21_30():
    assert compose_datetime_from("today", "21:30") == datetime.datetime.now()

@freeze_time("2024-02-23 21:30:00")
def test_compose_datetime_from_tomorrow_21_30():
    assert compose_datetime_from("tomorrow", "21:30") == datetime.datetime.now() + datetime.timedelta(days=1)
