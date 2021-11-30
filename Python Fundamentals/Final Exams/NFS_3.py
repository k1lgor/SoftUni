def drive(c, tok0, tok1, tok2):
    if c[tok0]['fuel'] < int(tok2):
        print("Not enough fuel to make that ride")
    else:
        c[tok0]['mile'] += int(tok1)
        c[tok0]['fuel'] -= int(tok2)
        print(
            f"{tok0} driven for {tok1} kilometers. {tok2} liters of fuel consumed.")
        if c[tok0]['mile'] >= 100000:
            del c[tok0]
            print(f"Time to sell the {tok0}!")
    return c


def refuel(c, tok0, tok1):
    c[tok0]['fuel'] += int(tok1)
    refueled = tok1 if c[tok0]['fuel'] < 75 else 75 - \
        c[tok0]['fuel'] + int(tok1)
    c[tok0]['fuel'] = min(c[tok0]['fuel'], 75)
    print(
        f"{tok0} refueled with {refueled} liters")
    return c


def revert(c, tok0, tok1):
    c[tok0]['mile'] -= int(tok1)
    if c[tok0]['mile'] < 10000:
        c[tok0]['mile'] = 10000
    else:
        print(f"{tok0} mileage decreased by {tok1} kilometers")
    return c


number = int(input())
cars = {}
for _ in range(number):
    car, mile, fuel = input().split("|")
    cars[car] = {'mile': int(mile), 'fuel': int(fuel)}

command = input()

while 'Stop' not in command:
    command, *tokens = command.split(" : ")

    if command == "Drive":
        drive(cars, tokens[0], tokens[1], tokens[2])

    elif command == "Refuel":
        refuel(cars, tokens[0], tokens[1])

    elif command == "Revert":
        revert(cars, tokens[0], tokens[1])

    command = input()

for k, v in sorted(cars.items(), key=lambda x: (-x[1]['mile'], x[0])):
    print(
        f"{k} -> Mileage: {v['mile']} kms, Fuel in the tank: {v['fuel']} lt.")
