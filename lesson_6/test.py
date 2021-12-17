class Counter:
    def __init__(self, name):
        self.name = name

        self._counts = {}

    def add_count(self, el, count):
        if el not in self._counts:
            self._counts[el] = 0

        self._counts[el] += count

    def get_counts(self):
        return self._counts

    def get_most_common(self):
        pass


counter = Counter(name="My counter!!!")
counter.add_count("a", 10)
counter.add_count("a", -15)
counter.add_count("b", 50)
counter.add_count("c", 100)
counter.add_count("d", 200)
print(counter.get_counts())

print(counter._counts)
tao = counter._counts

print(type(tao))
