fuel = input()
qnty = float(input())
card = input()
ttl = 0.0

if fuel == 'Diesel':
    ttl = qnty * (2.33 - 0.12) if card == 'Yes' else qnty * 2.33
elif fuel == 'Gas':
    ttl = qnty * (0.93 - 0.08) if card == 'Yes' else qnty * 0.93
elif fuel == 'Gasoline':
    ttl = qnty * (2.22 - 0.18) if card == 'Yes' else qnty * 2.22
if 20 < qnty <= 25:
    ttl *= 0.92
elif qnty > 25:
    ttl *= 0.9
print(f'{ttl:.2f} lv.')
