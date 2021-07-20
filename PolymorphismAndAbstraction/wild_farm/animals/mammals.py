from PolymorphismAndAbstraction.wild_farm.animals.animal import Mammal
from PolymorphismAndAbstraction.wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    _SOUND = 'Squeak'
    _FOOD_TYPES = (Vegetable, Fruit)
    _WEIGHT_INCREASE = 0.10


class Dog(Mammal):
    _SOUND = 'Woof!'
    _FOOD_TYPES = (Meat,)
    _WEIGHT_INCREASE = 0.40


class Cat(Mammal):
    _SOUND = 'Meow'
    _FOOD_TYPES = (Vegetable, Meat)
    _WEIGHT_INCREASE = 0.30


class Tiger(Mammal):
    _SOUND = 'ROAR!!!'
    _FOOD_TYPES = (Meat,)
    _WEIGHT_INCREASE = 1.00
