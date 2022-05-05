from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super(SaltwaterAquarium, self).__init__(name, 25)

    @property
    def fish_type(self):
        return 'SaltwaterFish'
