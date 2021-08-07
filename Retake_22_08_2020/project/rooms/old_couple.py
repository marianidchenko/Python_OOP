from Retake_22_08_2020.project.appliances.fridge import Fridge
from Retake_22_08_2020.project.appliances.stove import Stove
from Retake_22_08_2020.project.appliances.tv import TV
from Retake_22_08_2020.project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        budget = pension_one + pension_two
        super().__init__(family_name, budget, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)