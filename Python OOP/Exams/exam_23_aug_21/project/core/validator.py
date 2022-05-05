class Validator:
    @staticmethod
    def check_name(name, msg):
        if name.strip() == '':
            raise ValueError(msg)
