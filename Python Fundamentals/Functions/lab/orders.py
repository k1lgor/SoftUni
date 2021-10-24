menu = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
    }

def Order(product, quantity):
    if product in menu:
        price = menu[product] * quantity
        print(f'{price:.2f}')
        return price
        
Order(product = input(), quantity = int(input()))
