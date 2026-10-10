
from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, Newman") == 0


def test_hi():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hey there") == 20
    assert value("How are you?") == 20


def test_goodbye():
    assert value("goodbye") == 100
    assert value("Goodbye") == 100
    assert value("GOODBYE") == 100


def test_other():
    assert value("greetings") == 100
    assert value("Greetings") == 100
    assert value("GREETINGS") == 100
    assert value("What's up?") == 100


def test_whitespace():
    assert value("  hello") == 0
    assert value("  Hi  ") == 20
    assert value("  goodbye  ") == 100
