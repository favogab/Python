import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")


def test_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/2")


def test_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"