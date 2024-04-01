import pytest
import datetime

from functions.level_1.two_date_parser import compose_datetime_from

@pytest.fixture
def date_time_test_data():
    return {
        "today": "today",
        "tomorrow": "tomorrow",
        "today_date": datetime.date.today(),
        "tomorrow_date": datetime.date.today() + datetime.timedelta(days=1),
        "time": "12:30",
        "expected_today_hour": 12,
        "expected_today_minute": 30,
    }

@pytest.mark.parametrize("date_key,expected_date", [
    ("today", "today_date"),
    ("tomorrow", "tomorrow_date"),
])
def test__compose_datetime_from__date_changes(date_time_test_data, date_key, expected_date):
    result = compose_datetime_from(date_time_test_data[date_key], date_time_test_data["time"])
    assert result.date() == date_time_test_data[expected_date]

@pytest.mark.parametrize("date_key,expected_hour,expected_minute", [
    ("today", "expected_today_hour", "expected_today_minute"),
    ("tomorrow", "expected_today_hour", "expected_today_minute"),
])
def test__compose_datetime_from__time_does_not_change(date_time_test_data, date_key, expected_hour, expected_minute):
    result = compose_datetime_from(date_time_test_data[date_key], date_time_test_data["time"])
    assert result.hour == date_time_test_data[expected_hour]
    assert result.minute == date_time_test_data[expected_minute]
