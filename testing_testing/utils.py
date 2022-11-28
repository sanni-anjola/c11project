def add(a, b):
    return a + b


def square_list(numbers: list):
    return [num ** 2 for num in numbers]


class Counter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            num = self.start
            self.start += 1
            return num

        raise StopIteration


c = Counter(10, 18)

for counter in c:
    print(counter)
