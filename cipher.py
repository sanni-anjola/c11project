def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts celsius to fahrenheit
    """
    return celsius * 1.8 + 32


fahrenheit: float = celsius_to_fahrenheit(100)
print(fahrenheit)


# help(celsius_to_fahrenheit)

def func(lst):
    from collections import Counter

    d = Counter(lst)
    print(d)
    return [k for k, _ in sorted(d.items(), key=lambda x: x[1], reverse=True)]


# print(func("hello"))

def func2(lst):
    counter = {}

    for item in lst:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    print(counter)

func2("hello")

def func1(lst):
    from collections import defaultdict
    counter = defaultdict(int)

    for l in lst:
        counter[l] += 1

    return [k for k, _ in sorted(counter.items(), key=lambda x: x[1], reverse=True)]


# print(func1("hello"))
