class jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Wrong capacity value")
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return "🍪" * self._n

    def deposit(self, n):
        if self._n + n > self._capacity:
            raise ValueError("Not enough capacity")
        self._n = self._n + n

    def withdraw(self, n):
        if self._n < n:
            raise ValueError("Not enough cookies to be withdrawn")
        self._n = self._n - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n


my_jar = jar(10)
my_jar.deposit(8)
print(my_jar)
my_jar.withdraw(6)
print(my_jar)
