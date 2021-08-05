from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase):
        pass

