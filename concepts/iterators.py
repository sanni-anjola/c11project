# iterables

hello = iter(["hello", "how", "are", "you"])
print(next(hello))
print(next(hello))
# print(next(hello))
# print(next(hello))
# print(next(hello))
hello = iter(["hello", "how", "are", "you"])
print(list(hello))


class Counter:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):

        if self.start < self.stop:
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration


counter = Counter(2, 5, 2)

for count in counter:
    print(count)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
