from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def add_survivor(self, survivor:Survivor):
        pass

    def add_supply(self, supply: Supply):
        pass

    def add_medicine(self, medicine: Medicine):
        pass

    def heal(self, survivor: Survivor, medicine_type: str):
        pass

    def sustain(self, survivor:Survivor, sustenance_type: str):
        pass

    def next_day(self):
        pass
