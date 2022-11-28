# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
from dataclasses import dataclass, field


@dataclass(order=True)
class Human:
    agbado: tuple[int, str] = field(init=False, repr=False)
    name: str
    age: int = field(default=0)
    gender: str = field(default="F")
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)

    def __post_init__(self):
        self.agbado = (self.age, self.name)


human = Human("Ololade", 25, "F")
alien = Human("Boyo", 45, "M")

human.name = "Dorcas"
print(human < alien)
print(human)
x = sorted([alien, human])
print(x)
