mins = int(input())
daily = int(input())
cal = int(input())

ttl_mins = mins * daily
ttl_cal = ttl_mins * 5
half = cal / 2

if ttl_cal < half:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {ttl_cal}.')
else:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {ttl_cal}.')