from abc import ABC, abstractmethod


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        pass
