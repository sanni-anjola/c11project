from functools import lru_cache, wraps
from typing import Callable
from time import time


def function_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        print(f"Time taken for {func.__name__} to run is: {time() - start}")

    return wrapper


@function_timer
@lru_cache(maxsize=24)
def factorial_with_cache(num: int) -> int:
    if num <= 1:
        return 1
    return factorial_with_cache(num - 1)


@function_timer
def factorial(num: int) -> int:
    if num <= 1:
        return 1
    return factorial(num - 1)


print(factorial_with_cache(100))
print(factorial(100))
