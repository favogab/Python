from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello World!") == "Hll Wrld!"
    assert shorten("Favour") == "Fvr"

def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("Python3") == "Pythn3"