class Vehicle:
    def __init__(self, type_of, model, price):
        self.type_of = type_of
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            self.owner = owner
            return f"Successfully bought a {self.type_of}. Change: {money - self.price:.2f}"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type_of} is owned by: {self.owner}"
        return f"{self.model} {self.type_of} is on sale: {self.price}"


type_of = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(type_of, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
