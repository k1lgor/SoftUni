budget = float(input())
gender = input()
age = int(input())
sport = input()

if gender == 'm':
    if sport == 'Gym':
        price = 42
    elif sport == 'Boxing':
        price = 41
    elif sport == 'Yoga':
        price = 45
    elif sport == 'Zumba':
        price = 34
    elif sport == 'Dances':
        price = 51
    elif sport == 'Pilates':
        price = 39
if gender == 'f':
    if sport == 'Gym':
        price = 35
    elif sport == 'Boxing':
        price = 37
    elif sport == 'Yoga':
        price = 42
    elif sport == 'Zumba':
        price = 31
    elif sport == 'Dances':
        price = 53
    elif sport == 'Pilates':
        price = 37
ttl = price
if age <= 19:
    ttl *= 0.8
if ttl > budget:
    print(f'You don\'t have enough money! You need ${abs(ttl - budget):.2f} more.')
else:
    print(f'You purchased a 1 month pass for {sport}.')