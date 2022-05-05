from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name: str):
        super(Geodesist, self).__init__(name, 50)
