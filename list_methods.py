import random


# random.seed(45)
# rng = list(range(1, 100, 5))
# print(rng)
#
# random.shuffle(rng)
# print(rng)
# rng.sort(reverse=True)
# print(rng)
# print(random.choice(rng))

# fruits = ["apple", "mango", "water melon", "cherry", "banana", "cucumber", "pineapple", "orange"]
# fruits.sort(key=len)
# print(fruits)

# lst = [int(input(f"Enter student {i}'s score: ")) for i in range(1, 6)]
# print(lst)
# print("Total Scores = ", sum(lst))
# print("Max = ", max(lst))
# print("Min = ", min(lst))
# print("Average = ", sum(lst) / len(lst))


def is_prime(num: int) -> bool:
    import math

    if num <= 1:
        return False
    if num == 2:
        return True
    max_divisor = math.ceil(math.sqrt(num)) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True


primes = {k: v for k, v in enumerate(range(1, 10)) if is_prime(v)}
print(type(primes))
print(primes)

# def cube(num: int) -> int:
#     return num ** 3
#
#
# cubes = [cube(i) for i in range(1, 11)]
# print(cubes)
