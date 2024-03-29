from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def min_table_number(self):
        return 51

    @property
    def max_table_number(self):
        return 100

    @property
    def table_number_error_msg(self):
        return "Outside table's number must be between 51 and 100 inclusive!"
