import math
year = input()
holidays = int(input())
weekends = int(input())

weekends_insofia = 48 - weekends
playing_saturdays = weekends_insofia * 3 / 4
holidays_insofia = holidays * 2 / 3
ttl = playing_saturdays + holidays_insofia + weekends

if year == 'leap':
    ttl *= 1.15
print(math.floor(ttl))
