budget = float(input())
needed_fuel = float(input())
day = input()

price_fuel = needed_fuel * 2.1
ttl = 100 + price_fuel
if day == 'Saturday':
    ttl *= 0.9
else:
    ttl *= 0.8
if ttl > budget:
    print(f'Not enough money! Money needed: {abs(ttl - budget):.2f} lv.')
else:
    print(f'Safari time! Money left: {abs(ttl - budget):.2f} lv.')