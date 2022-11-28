import time
from functools import wraps
# import functools


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print("About to be decorated")
        value = func(*args, **kwargs)
        print("Just decorated")
        return value

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        time_taken = time.perf_counter() - start
        print(f"{func.__name__} took {time_taken:.2E}secs to run")
        return val

    return wrapper


@print_decorator
def printer():
    return "I am a printer"


# @print_decorator
@timer
def factorial(num: int) -> int:
    """
    Calculates the factorial of num
    :param num:
    :return factorial of num:
    """
    import math
    return math.factorial(num)


@timer
def my_factorial(num: int) -> int:
    prod = 1
    for i in range(num, 0, -1):
        prod *= i
    return prod


# printer = print_decorator(printer)

# print(printer())
# print(factorial(500))
# print(my_factorial(500))
print(factorial.__name__)
print(factorial.__doc__)
