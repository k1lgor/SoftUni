from project.decoration.decoration_repository import DecorationRepository

from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        except ValueError as e:
            return str(e)

    def add_decoration(self, decoration_type: str):
        try:
            decoration = self.decoration_factory.create_decoration(decoration_type)
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        except ValueError as e:
            return str(e)

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if (decoration := self.decorations_repository.find_by_type(decoration_type)) == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        self.decorations_repository.remove(decoration)
        if (aquarium := self.__find_aquarium_by_name(aquarium_name)) is None:
            return
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        try:
            fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
            aquarium = self.__find_aquarium_by_name(aquarium_name)
            return aquarium.add_fish(fish)
        except ValueError as e:
            return str(e)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        value = sum(x.price for x in aquarium.fish) + sum(x.price for x in aquarium.decorations)
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return ''.join(f'{str(aquarium)}\n' for aquarium in self.aquariums).strip()

    def __find_aquarium_by_name(self, aquarium_name):
        return next((aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name), None)
