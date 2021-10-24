from math import ceil
dist = 384400 #km
speed = float(input())
ltr = float(input()) #100km

go_and_back = dist * 2
time = ceil(go_and_back / speed)
ttl_time = 3 + time
fuel = (ltr * go_and_back) / 100
print(f'{ttl_time}\n{fuel:.0f}')