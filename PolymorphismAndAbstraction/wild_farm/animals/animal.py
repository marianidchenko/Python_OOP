from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def make_sound(self):
        return self._SOUND

    def feed(self, food):
        if not isinstance(food, self._FOOD_TYPES):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.food_eaten += food.quantity
            self.weight += self._WEIGHT_INCREASE * food.quantity

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten=food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten=food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"