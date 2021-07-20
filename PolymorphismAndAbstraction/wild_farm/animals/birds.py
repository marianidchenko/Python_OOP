from PolymorphismAndAbstraction.wild_farm.animals.animal import Bird
from PolymorphismAndAbstraction.wild_farm.food import Meat, Food


class Owl(Bird):
    _SOUND = 'Hoot Hoot'
    _FOOD_TYPES = (Meat, )
    _WEIGHT_INCREASE = 0.25


class Hen(Bird):
    _SOUND = 'Cluck'
    _FOOD_TYPES = (Food, )
    _WEIGHT_INCREASE = 0.35
