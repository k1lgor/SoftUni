from abc import ABC, abstractmethod

from project.core.validator import Validator
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f'{self.name}:\n'
        if self.fish:
            result += f'Fish: {" ".join(x.name for x in self.fish)}\n'
        else:
            result += 'none\n'
        result += f'Decorations: {len(self.decorations)}\n' \
                  f'Comfort: {self.calculate_comfort()}'
        return result
