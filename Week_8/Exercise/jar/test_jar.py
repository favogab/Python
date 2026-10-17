
import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    custom_jar = Jar(5)
    assert custom_jar.capacity == 5
    assert custom_jar.size == 0


def test_invalid_capacity():
    for capacity in [-1, 2.5, "12", True]:
        with pytest.raises(ValueError):
            Jar(capacity)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)

    jar.deposit(4)
    assert jar.size == 4

    jar.deposit(6)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(1)

    # A rejected deposit must not change the jar.
    assert jar.size == 10


def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)

    jar.withdraw(3)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(5)

    assert jar.size == 4


def test_invalid_amounts():
    jar = Jar()

    for amount in [-1, 1.5, "3", True]:
        with pytest.raises(ValueError):
            jar.deposit(amount)

        with pytest.raises(ValueError):
            jar.withdraw(amount)

    assert jar.size == 0
