month = input()
overnight = int(input())
apart = 0.0
stud = 0.0

if month in ['May', 'October']:
    apart = overnight * 65
    stud = overnight * 50
    if overnight > 14:
        stud *= 0.7
        apart *= 0.9
    elif 14 > overnight > 7:
        stud *= 0.95
elif month in ['June', 'September']:
    apart = overnight * 68.7
    stud = overnight * 75.2
    if overnight > 14:
        stud *= 0.8
        apart *= 0.9
elif month in ['July', 'August']:
    apart = overnight * 77
    stud = overnight * 76
    if overnight > 14:
        apart *= 0.9
print(f'Apartment: {apart:.2f} lv.\nStudio: {stud:.2f} lv.')
