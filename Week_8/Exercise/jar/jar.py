
class Jar:
    def __init__(self, capacity=12):
        # A jar must have a valid, non-negative capacity.
        if type(capacity) is not int or capacity < 0:
            raise ValueError("Invalid capacity")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Display one cookie emoji for each cookie in the jar.
        return "🍪" * self._size

    def deposit(self, n):
        if type(n) is not int or n < 0:
            raise ValueError("Invalid deposit amount")

        if self._size + n > self._capacity:
            raise ValueError("Jar capacity exceeded")

        self._size += n

    def withdraw(self, n):
        if type(n) is not int or n < 0:
            raise ValueError("Invalid withdrawal amount")

        if n > self._size:
            raise ValueError("Not enough cookies")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
