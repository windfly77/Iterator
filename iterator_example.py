class Licznik:
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
            return liczba


# Użycie iteratora
for liczba in Licznik(1, 5):
    print(liczba)
print("\n\n\\\\\n")
class OdwrotnyIterator:
    def __init__(self, kolekcja):
        self.kolekcja = kolekcja
        self.indeks = len(kolekcja)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks == 0:
            raise StopIteration
        self.indeks -= 1
        return self.kolekcja[self.indeks]


# Użycie
for element in OdwrotnyIterator(["A", "B", "C", "D"]):
    print(element)