from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        total_members = 2 + len(children)
        budget = salary_one + salary_two
        super().__init__(family_name, budget, total_members)
        self.appliances = [TV(), Fridge(), Laptop()] * total_members
        self.room_cost = 30
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)
