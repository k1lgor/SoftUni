chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
ttl = 0.0

if season in ['Spring', 'Summer']:
    ttl = chrysanthemums * 2 + roses * 4.1 + tulips * 2.5
    if holiday == 'Y':
        ttl = chrysanthemums * 2 * 1.15 + roses * 4.1 * 1.15 + tulips * 2.5 * 1.15
    if tulips > 7 and season == 'Spring':
        ttl *= 0.95
    if chrysanthemums + roses + tulips > 20:
        ttl *= 0.8
elif season in ['Winter', 'Autumn']:
    ttl = chrysanthemums * 3.75 + roses * 4.5 + tulips * 4.15
    if holiday == 'Y':
        ttl = chrysanthemums * 3.75 * 1.15 + roses * 4.5 * 1.15 + tulips * 4.15 * 1.15
    if roses >= 10 and season == 'Winter':
        ttl *= 0.9
    if chrysanthemums + roses + tulips > 20:
        ttl *= 0.8

print(f'{(ttl + 2):.2f}')
