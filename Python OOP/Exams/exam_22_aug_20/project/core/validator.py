class Validator:
    @staticmethod
    def check_number(number, msg):
        if number < 0:
            raise ValueError(msg)
