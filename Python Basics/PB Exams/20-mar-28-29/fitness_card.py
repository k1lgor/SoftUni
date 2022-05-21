budget = float(input())
gender = input()
age = int(input())
sport = input()

if gender == 'f':
    if sport in ['Boxing', 'Pilates']:
        price = 37
    elif sport == 'Dances':
        price = 53
    elif sport == 'Gym':
        price = 35
    elif sport == 'Yoga':
        price = 42
    elif sport == 'Zumba':
        price = 31
elif gender == 'm':
    if sport == 'Boxing':
        price = 41
    elif sport == 'Dances':
        price = 51
    elif sport == 'Gym':
        price = 42
    elif sport == 'Pilates':
        price = 39
    elif sport == 'Yoga':
        price = 45
    elif sport == 'Zumba':
        price = 34
ttl = price
if age <= 19:
    ttl *= 0.8
if ttl > budget:
    print(f'You don\'t have enough money! You need ${abs(ttl - budget):.2f} more.')
else:
    print(f'You purchased a 1 month pass for {sport}.')