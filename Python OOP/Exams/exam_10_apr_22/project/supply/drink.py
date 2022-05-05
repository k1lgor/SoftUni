from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str, energy=15):
        super(Drink, self).__init__(name, energy)
