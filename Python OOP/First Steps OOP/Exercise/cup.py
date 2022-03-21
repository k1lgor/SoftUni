class Cup:
    def __init__(self, size, quantity):
        self.amount = None
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        self.amount = amount
        if self.size >= self.quantity + self.amount:
            self.quantity += self.amount

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
