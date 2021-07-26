from PolymorphismAndAbstraction.animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, Kitten._GENDER)

    _GENDER = 'Female'

    def make_sound(self):
        return f"Meow"