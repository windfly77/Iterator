class EvenIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            liczba = self.current
            self.current += 1
            if self.current%2 != 0:
                print(liczba)

for liczba in EvenIterator(1, 10):
    print(liczba)

#Checking for commit