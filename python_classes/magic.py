class Person:

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name} and {self.age}yrs old"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __format__(self, format_spec):
        if format_spec == 'n':
            return self.name
        else:
            return str(self)

    def __len__(self):
        return 6

omotee = Person(name="Omotola", age=20)
shafspecs = Person(name="AbdurRahman", age=25)

print(f"{omotee:n}")
print(omotee < shafspecs)
print(len(shafspecs))
# omotee.why = "wia"

print(omotee.__dict__)



