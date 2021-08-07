from Retake_22_08_2020.project.appliances.fridge import Fridge
from Retake_22_08_2020.project.appliances.laptop import Laptop
from Retake_22_08_2020.project.appliances.tv import TV
from Retake_22_08_2020.project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        budget = salary_one + salary_two
        super().__init__(family_name, budget, 2)
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.room_cost = 20
        self.calculate_expenses(self.appliances)