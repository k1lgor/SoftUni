from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    def __init__(self, name: str):
        super(Meteorologist, self).__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15
