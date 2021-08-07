from Retake_19_12_2020.project.medicine.medicine import Medicine
from Retake_19_12_2020.project.supply.supply import Supply
from Retake_19_12_2020.project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if not food_list:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_list = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        if not water_list:
            raise IndexError("There are no water supplies left!")
        return water_list

    @property
    def painkillers(self):
        painkiller_list = [x for x in self.supplies if x.__class__.__name__ == "Painkiller"]
        if not painkiller_list:
            raise IndexError("There are no painkillers left!")
        return painkiller_list

    @property
    def salves(self):
        salves_list = [x for x in self.supplies if x.__class__.__name__ == "Salve"]
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor:Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine_used = [x for x in self.medicine if x.__class__.__name__ == medicine_type][-1]
            self.medicine.remove(medicine_used)
            medicine_used.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor:Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance_used = [x for x in self.supplies if x.__class__.__name__ == sustenance_type][-1]
            self.supplies.remove(sustenance_used)
            sustenance_used.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "WaterSupply")
            self.sustain(survivor, "FoodSupply")
