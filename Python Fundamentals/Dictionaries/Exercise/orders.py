command = input()
order = {}

while 'buy' not in command:
    tokens = command.split()
    name = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    if name not in order:
        order[name] = {"price": price, "quantity": quantity}
    else:
        order[name]["price"] = price
        order[name]["quantity"] += quantity

    command = input()

for name in order.items():
    print(f"{name[0]} -> {(name[1]['price'] * name[1]['quantity']):.2f}")
