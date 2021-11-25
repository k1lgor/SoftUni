number = int(input())
cars = {}
for _ in range(number):
    car, mile, fuel = input().split("|")
    cars[car] = {'mile': int(mile), 'fuel': int(fuel)}

command = input()

while 'Stop' not in command:
    command, *tokens = command.split(" : ")

    if command == "Drive":
        if cars[tokens[0]]['fuel'] < int(tokens[2]):
            print("Not enough fuel to make that ride")
        else:
            cars[tokens[0]]['mile'] += int(tokens[1])
            cars[tokens[0]]['fuel'] -= int(tokens[2])
            print(
                f"{tokens[0]} driven for {tokens[1]} kilometers. {tokens[2]} liters of fuel consumed.")
            if cars[tokens[0]]['mile'] >= 100000:
                del cars[tokens[0]]
                print(f"Time to sell the {tokens[0]}!")

    elif command == "Refuel":
        cars[tokens[0]]['fuel'] += int(tokens[1])
        if cars[tokens[0]]['fuel'] < 75:
            refueled = tokens[1]
        else:
            refueled = 75 - cars[tokens[0]]['fuel'] + int(tokens[1])
        cars[tokens[0]]['fuel'] = min(cars[tokens[0]]['fuel'], 75)
        print(
            f"{tokens[0]} refueled with {refueled} liters")

    elif command == "Revert":
        cars[tokens[0]]['mile'] -= int(tokens[1])
        if cars[tokens[0]]['mile'] < 10000:
            cars[tokens[0]]['mile'] = 10000
        else:
            print(f"{tokens[0]} mileage decreased by {tokens[1]} kilometers")

    command = input()

for k, v in sorted(cars.items(), key=lambda x: (-x[1]['mile'], x[0])):
    print(
        f"{k} -> Mileage: {v['mile']} kms, Fuel in the tank: {v['fuel']} lt.")
