# from typing import Self


class Person:
    number_of_persons = 0

    def __init__(self, name: str, age=17) -> None:
        self._name = name
        self._age = age
        Person.number_of_persons += 1

    @classmethod
    def get_number_of_persons(cls):
        return cls.number_of_persons

    @staticmethod
    def determine_class(age: int) -> str:
        if age >= 18:
            return "Major"
        return "Minor"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        print("Name will now be deleted")
        del self._name


person1 = Person("Abigail")
person12 = Person("Dorcas", 56)
print(person1.name)
person1.name = "Omotee"

# person1.age = -2
# del person1.name
#
# print(person1.name)
person1.number_of_persons = 7
print(Person.number_of_persons)
print(person1.number_of_persons)
print(person12.number_of_persons)
print(dir(person1))

print(Person.determine_class(56))
