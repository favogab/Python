
from datetime import date
import pytest

from seasons import parse_birthdate, calculate_minutes


def test_valid_birthdates():
    assert parse_birthdate("2000-01-01") == date(2000, 1, 1)
    assert parse_birthdate("2024-02-29") == date(2024, 2, 29)


def test_invalid_birthdates():
    # Reject impossible dates and malformed input.
    with pytest.raises(ValueError):
        parse_birthdate("2023-02-29")

    with pytest.raises(ValueError):
        parse_birthdate("2000-13-01")

    with pytest.raises(ValueError):
        parse_birthdate("January 1, 2000")

    with pytest.raises(ValueError):
        parse_birthdate("2000-1-1")

    with pytest.raises(ValueError):
        parse_birthdate("2000/01/01")


def test_one_year():
    birthday = date(2023, 1, 1)
    today = date(2024, 1, 1)

    assert calculate_minutes(birthday, today) == 525600


def test_leap_year():
    # This date range includes February 29, 2024.
    birthday = date(2024, 1, 1)
    today = date(2025, 1, 1)

    assert calculate_minutes(birthday, today) == 527040


def test_future_birthdate():
    with pytest.raises(ValueError):
        calculate_minutes(date(2030, 1, 1), date(2026, 1, 1))


def test_same_day():
    assert calculate_minutes(date(2026, 1, 1), date(2026, 1, 1)) == 0
