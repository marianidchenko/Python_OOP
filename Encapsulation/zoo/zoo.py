from Encapsulation.zoo.caretaker import Caretaker
from Encapsulation.zoo.cheetah import Cheetah
from Encapsulation.zoo.keeper import Keeper
from Encapsulation.zoo.lion import Lion
from Encapsulation.zoo.tiger import Tiger
from Encapsulation.zoo.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animals"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_due = sum(map(lambda worker: worker.salary, self.workers))
        if total_due <= self.__budget:
            self.__budget -= total_due
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_due = sum(map(lambda animal: animal.money_for_care, self.animals))
        if total_due <= self.__budget:
            self.__budget -= total_due
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        total_lions = 0
        lions_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                total_lions += 1
                lions_info.append(repr(animal))

        total_tigers = 0
        tigers_info = []
        for animal in self.animals:
            if type(animal) == Tiger:
                total_tigers += 1
                tigers_info.append(repr(animal))

        total_cheetahs = 0
        cheetahs_info = []
        for animal in self.animals:
            if type(animal) == Cheetah:
                total_cheetahs += 1
                cheetahs_info.append(repr(animal))

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {total_lions} Lions:\n"
        result += '\n'.join(lions_info) + "\n"
        result += f"----- {total_tigers} Tigers:\n"
        result += '\n'.join(tigers_info) + "\n"
        result += f"----- {total_tigers} Cheetahs:\n"
        result += '\n'.join(cheetahs_info)

        return result

    def workers_status(self):

        total_keepers = 0
        keepers_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                total_keepers += 1
                keepers_info.append(repr(worker))

        total_caretakers = 0
        caretakers_info = []
        for worker in self.workers:
            if type(worker) == Caretaker:
                total_caretakers += 1
                caretakers_info.append(repr(worker))

        total_vets = 0
        vets_info = []
        for worker in self.workers:
            if type(worker) == Vet:
                total_vets += 1
                vets_info.append(repr(worker))

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {total_keepers} Keepers:\n"
        result += '\n'.join(keepers_info) + "\n"
        result += f"----- {total_caretakers} Caretakers:\n"
        result += '\n'.join(caretakers_info) + "\n"
        result += f"----- {total_vets} Vets:\n"
        result += '\n'.join(vets_info)

        return result
