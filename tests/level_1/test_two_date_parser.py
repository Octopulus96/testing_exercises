import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from


@pytest.fixture(name="date_time")
def fixture_date_time() -> dict[str, str | datetime.date | int]:
    return {
        "today": "today",
        "tomorrow": "tomorrow",
        "today_date": datetime.date.today(),
        "tomorrow_date": datetime.date.today() + datetime.timedelta(days=1),
        "time": "12:30",
        "expected_today_hour": 12,
        "expected_today_minute": 30,
    }


@pytest.mark.parametrize(
    "date_key,expected_date",
    [
        ("today", "today_date"),
        ("tomorrow", "tomorrow_date"),
    ],
)
def test__compose_datetime_from__date_changes(
    date_time: dict,
    date_key: str,
    expected_date: str,
) -> None:
    result: datetime.datetime = compose_datetime_from(date_time[date_key], date_time["time"])
    assert result.date() == date_time[expected_date]


@pytest.mark.parametrize(
    "date_key,expected_hour,expected_minute",
    [
        ("today", "expected_today_hour", "expected_today_minute"),
        ("tomorrow", "expected_today_hour", "expected_today_minute"),
    ],
)
def test__compose_datetime_from__time_does_not_change(
    date_time: dict,
    date_key: str,
    expected_hour: str,
    expected_minute: str,
) -> None:
    result: datetime.datetime = compose_datetime_from(date_time[date_key], date_time["time"])
    assert result.hour == date_time[expected_hour]
    assert result.minute == date_time[expected_minute]
