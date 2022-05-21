season = input()
km = float(input())
ttl = 0.0
if 10000 < km <= 20000:
    ttl = km * 1.45 * 4
elif 5000 < km <= 10000:
    if season in ['Spring', 'Autumn']:
        ttl = km * 0.95 * 4
    elif season == 'Summer':
        ttl = km * 1.1 * 4
    else:
        ttl = km * 1.25 * 4
elif season in ['Spring', 'Autumn']:
    ttl = km * 0.75 * 4
elif season == 'Summer':
    ttl = km * 0.9 * 4
else:
    ttl = km * 1.05 * 4

print(f'{(ttl * 0.9):.2f}')
