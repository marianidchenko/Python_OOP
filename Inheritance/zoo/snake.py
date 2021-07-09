from Inheritance.zoo.lizard import Lizard
from Inheritance.zoo.reptile import Reptile
from Inheritance.zoo.mammal import Mammal


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)