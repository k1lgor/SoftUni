class Validator:
    @staticmethod
    def check_empty_string(name, msg):
        if name.strip() == '':
            raise ValueError(msg)

    @staticmethod
    def check_price(price, msg):
        if price <= 0:
            raise ValueError(msg)
