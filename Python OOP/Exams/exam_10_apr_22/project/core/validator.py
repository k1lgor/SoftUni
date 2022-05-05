class Validator:
    @staticmethod
    def check_if_name_is_empty(name, msg):
        if name == '':
            raise ValueError(msg)

    @staticmethod
    def check_if_energy_is_negative(value, msg):
        if value < 0:
            raise ValueError(msg)

    @staticmethod
    def check_if_age_is_under_12(value, msg):
        if value < 12:
            raise ValueError(msg)

    @staticmethod
    def check_if_stamina_is_less_than_0_or_more_than_100(value, msg):
        if value < 0 or value > 100:
            raise ValueError(msg)
