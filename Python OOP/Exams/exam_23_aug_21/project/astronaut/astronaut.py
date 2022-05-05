from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_name(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        result = f'Name: {self.name}\n'
        result += f'Oxygen: {self.oxygen}'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"
        return result
