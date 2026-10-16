
from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True


def test_invalid_ranges():
    assert validate("300.1.1.1") is False
    assert validate("192.300.1.1") is False
    assert validate("192.168.300.1") is False
    assert validate("192.168.1.300") is False


def test_invalid_formats():
    assert validate("192.168.1") is False
    assert validate("192.168.1.1.5") is False
    assert validate("192.168.1.1000") is False
    assert validate("cat") is False
    assert validate("192.168.001.1") is False
    assert validate("192.168.1.a") is False
