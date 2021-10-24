budget = int(input())
season = input()
fishermen = int(input())

discount = 0.0

if fishermen <= 6:
    if season == 'Spring':
        discount = 3000 * 0.9
    elif season in ['Summer', 'Autumn']:
        discount = 4200 * 0.9
    else:
        discount = 2600 * 0.9
elif 7 <= fishermen <= 11:
    if season == 'Spring':
        discount = 3000 * 0.85
    elif season in ['Summer', 'Autumn']:
        discount = 4200 * 0.85
    else:
        discount = 2600 * 0.85
else:
    if season == 'Spring':
        discount = 3000 * 0.75
    elif season in ['Summer', 'Autumn']:
        discount = 4200 * 0.75
    else:
        discount = 2600 * 0.75
if fishermen % 2 == 0 and season != "Autumn":
    discount *= 0.95
if budget < discount:
    print(f'Not enough money! You need {abs(budget - discount):.2f} leva.')
else:
    print(f'Yes! You have {abs(budget - discount):.2f} leva left.')
