import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return round(math.hypot(self.x, self.y), 2)

    def __add__(self, other):
        print("Another")
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        print("I was called")
        return self + other

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"


v1 = Vector(1, -5)
v2 = Vector(2, 2)
print(v1)
print(abs(v1))
v3 = v1 + v2
v1 += v2
print(v1)
print(v3)
