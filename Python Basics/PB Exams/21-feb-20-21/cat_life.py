from math import floor as fl
breed = input()
gender = input()
year = 0

if breed not in ['British Shorthair', 'Siamese', 'Persian', 'Ragdoll', 'American Shorthair', 'Siberian']:
    print(f'{breed} is invalid cat!')

else:
    if gender == 'f':
        if breed == 'American Shorthair':
            year = 13 * 12 / 6
        elif breed == 'British Shorthair':
            year = 14 * 12 / 6
        elif breed == 'Persian':
            year = 15 * 12 / 6
        elif breed == 'Ragdoll':
            year = 17 * 12 / 6
        elif breed == 'Siamese':
            year = 16 * 12 / 6
        elif breed == 'Siberian':
            year = 12 * 12 / 6
    elif gender == 'm':
        if breed == 'American Shorthair':
            year = 12 * 12 / 6
        elif breed == 'British Shorthair':
            year = 13 * 12 / 6
        elif breed == 'Persian':
            year = 14 * 12 / 6
        elif breed == 'Ragdoll':
            year = 16 * 12 / 6
        elif breed == 'Siamese':
            year = 15 * 12 / 6
        elif breed == 'Siberian':
            year = 11 * 12 / 6
    print(f'{fl(year)} cat months')