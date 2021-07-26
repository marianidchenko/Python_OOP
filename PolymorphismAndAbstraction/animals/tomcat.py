from PolymorphismAndAbstraction.animals.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, Tomcat._GENDER)

    _GENDER = 'Male'

    def make_sound(self):
        return f"Hiss"