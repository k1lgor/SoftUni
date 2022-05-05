class Validator:
    @staticmethod
    def table_number_not_in_range(number: int, min_val: int, max_val: int, msg: str):
        if number < min_val or number > max_val:
            raise ValueError(msg)
