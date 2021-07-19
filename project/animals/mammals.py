from project.animals.animal import Mammal


class Mouse(Mammal):
    _SOUND = 'Squeak'


class Dog(Mammal):
    _SOUND = 'Woof!'


class Cat(Mammal):
    _SOUND = 'Meow'


class Tiger(Mammal):
    _SOUND = 'ROAR!!!'
