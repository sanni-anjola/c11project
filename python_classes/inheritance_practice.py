class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("I am barking")


class Dog(Animal):
    def __init__(self, name, breed, color="Brown"):
        self.color = color
        super().__init__(name, breed)


class Cat(Animal):
    pass


dog = Dog("Max", "Golden retriever", "Blue")
dog.speak()
print(dog.name)
print(dog.breed)

d = Dog(*vars(dog))
print(d.name)
