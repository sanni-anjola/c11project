__all__ = ['add', 'sub']


def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


if __name__ == '__main__':
    print("I am invisible to other modules")
    print("Mod 1", __name__)

    print(add(4, 7))
