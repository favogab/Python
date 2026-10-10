
from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False


def test_first_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C1") == False
    assert is_valid("12AB") == False


def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("CS50P") == False
    assert is_valid("AB1C2") == False


def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB0") == False
    assert is_valid("CS50") == True
    assert is_valid("AB10") == True


def test_alphanumeric():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("AB-12") == False
    assert is_valid("AB12") == True
