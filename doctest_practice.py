# import doctest
#

def add(a, b):
    """
    >>> add(3, 5)
    8
    >>> add(3, "Hi")
    Traceback (most recent call last) # doctest: +IGNORE_EXCEPTION_DETAIL
        ...
    TypeError:
    """
    return a + b


# if __name__ == '__main__':
#     doctest.testmod()
