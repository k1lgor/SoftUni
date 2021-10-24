fuel = input()
liter = float(input())

if fuel in ['Gas', 'Gasoline', 'Diesel']:
    if liter >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')
