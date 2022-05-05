from project.core.validator import Validator


class Player:
    PLAYER_NAMES = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = bool
        self.need_sustenance = self.stamina != 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_name_is_empty(value, "Name not valid!")
        if value in Player.PLAYER_NAMES:
            raise Exception(f"Name {value} is already used!")
        Player.PLAYER_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.check_if_age_is_under_12(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.check_if_stamina_is_less_than_0_or_more_than_100(value, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        if self.stamina < 100:
            self.need_sustenance = True
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'
