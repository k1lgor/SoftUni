from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_success = 0
        self.mission_failed = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__create_astro(astronaut_type, name)
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        if (astronaut := self.astronaut_repository.find_by_name(name)) is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if (planet := self.planet_repository.find_by_name(planet_name)) is None:
            raise Exception("Invalid planet name!")
        astronauts = self.astronaut_repository.find_astro_for_mission(5, 30)
        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        astro_on_mission = 0
        for astro in astronauts:
            if len(planet.items) == 0:
                break
            while astro.oxygen > 0 and len(planet.items) > 0:
                astro.backpack.append(planet.items.pop())
                astro.breathe()
            astro_on_mission += 1
        if len(planet.items) == 0:
            self.mission_success += 1
            return f"Planet: {planet_name} was explored. {astro_on_mission} astronauts participated in collecting items."
        self.mission_failed += 1
        return "Mission is not completed."

    def report(self):
        result = f'{self.mission_success} successful missions!\n'
        result += f'{self.mission_failed} missions were not completed!\n'
        result += f'Astronauts\' info:\n'
        for astro in self.astronaut_repository.astronauts:
            result += str(astro) + '\n'

        return result.strip()

    def __create_astro(self, astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        elif astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        elif astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")
