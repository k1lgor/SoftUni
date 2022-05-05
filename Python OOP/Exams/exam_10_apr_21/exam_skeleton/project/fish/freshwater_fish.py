from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    EAT_INCR = 3

    def __init__(self, name: str, species: str, price: float):
        super(FreshwaterFish, self).__init__(name, species, 3, price)
