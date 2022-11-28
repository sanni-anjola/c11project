import abc


class Animal(abc.ABC):
    # __metaclass__ = abc.ABCMeta
    def name(self):
        return "Animal"

    @abc.abstractmethod
    def speak(self):
        return


class Dog(Animal):
    def name(self):
        return super().name() + " -> " + "Dog"

    # def speak(self):
    #     return "gbo"


class Cat(Animal):
    def speak(self):
        return "meu"


dog = Dog()
cat = Cat()

print(dog.speak())
print(dog.name())
print(cat.speak())
