from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    EAT_INCR = 2

    def __init__(self, name: str, species: str, price: float):
        super(SaltwaterFish, self).__init__(name, species, 5, price)
