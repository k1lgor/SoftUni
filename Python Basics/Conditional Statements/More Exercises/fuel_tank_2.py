fuel = input()
qnty = float(input())
card = input()
ttl = 0.0

if fuel == 'Gasoline':
    ttl = qnty * 2.22
    if card == 'Yes':
        ttl = qnty * (2.22 - 0.18)
elif fuel == 'Diesel':
    ttl = qnty * 2.33
    if card == 'Yes':
        ttl = qnty * (2.33 - 0.12)
elif fuel == 'Gas':
    ttl = qnty * 0.93
    if card == 'Yes':
        ttl = qnty * (0.93 - 0.08)

if 20 < qnty <= 25:
    ttl *= 0.92
elif qnty > 25:
    ttl *= 0.9
print(f'{ttl:.2f} lv.')
