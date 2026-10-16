
import pytest
from working import convert


def test_regular_hours():
    # Both times should work with or without minutes.
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_overnight_and_noon():
    # Overnight shifts and the 12 AM/PM boundary need special care.
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"
    assert convert("11 PM to 1 AM") == "23:00 to 01:00"


def test_invalid_times():
    # Hours outside 1–12 and minutes outside 0–59 must fail.
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5:99 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")


def test_invalid_formats():
    # Only the supported 12-hour formats should be accepted.
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9:5 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 am to 5 pm")

    with pytest.raises(ValueError):
        convert("9 AM to 5 PM extra")
