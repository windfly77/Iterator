class ParzysteIterator:
    def __init__(self, start, stop):
        self.current = start if start % 2 == 0 else start + 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        liczba = self.current
        self.current += 2
        return liczba


# Test
for liczba in ParzysteIterator(1, 10):
    print(liczba)