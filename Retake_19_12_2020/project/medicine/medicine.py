from abc import ABC, abstractmethod

from Retake_19_12_2020.project.survivor import Survivor


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        self.health_increase = health_increase

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        else:
            self._health_increase = value

    def apply(self, survivor:Survivor):
        survivor.health += self.health_increase
