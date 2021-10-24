naylon = int(input())
paint = int(input())
thinner = int(input())
hrs = int(input())

naylon = (naylon + 2) * 1.5
paint *= 14.5 * 1.1
thinner *= 5
ttl = 0.4 + naylon + paint + thinner
onehour = ttl * 0.3 * hrs

print(f'Total expenses: {(ttl + onehour):.2f} lv.')
