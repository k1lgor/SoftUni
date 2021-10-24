budget = float(input())
season = input()
car = ''
clas = ''
nl = '\n'
if budget > 500:
    clas = 'Luxury class'
    car = 'Jeep'
    budget *= 0.9
elif 100 < budget <= 500:
    clas = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        budget *= 0.45
    else:
        car = 'Jeep'
        budget *= 0.8
else:
    clas = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        budget *= 0.35
    else:
        car = 'Jeep'
        budget *= 0.65

print(f'{clas}{nl}{car} - {budget:.2f}')
