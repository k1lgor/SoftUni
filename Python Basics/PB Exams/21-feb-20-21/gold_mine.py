locations = int(input())
avr_gold_per_day = 0
working_days = 0
ttl = 0
extract = 0
for i in range(locations):
    avr_gold_per_day = float(input())
    days = int(input())
    ttl = 0
    for j in range(days):
        extract = float(input())
        ttl += extract
    ttl /= days
    if ttl >= avr_gold_per_day:
        print(f'Good job! Average gold per day: {ttl:.2f}.')

    else:
        print(f'You need {abs(avr_gold_per_day - ttl):.2f} gold.')
