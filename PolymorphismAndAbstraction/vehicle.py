from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        actual_consumption = self.fuel_consumption + Car.AC_CONSUMPTION
        if self.fuel_quantity/distance >= actual_consumption:
            self.fuel_quantity -= distance * actual_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        actual_consumption = self.fuel_consumption + Truck.AC_CONSUMPTION
        if self.fuel_quantity / distance >= actual_consumption:
            self.fuel_quantity -= distance * actual_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)