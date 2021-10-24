stage = input()
ticket = input()
num_tickets = int(input())
photo = input()
ttl = 0

if stage == 'Quarter final':
    if ticket == 'Standard':
        ttl = num_tickets * 55.5
    elif ticket == 'Premium':
        ttl = num_tickets * 105.2
    elif ticket == 'VIP':
        ttl = num_tickets * 118.9
elif stage == 'Semi final':
    if ticket == 'Standard':
        ttl = num_tickets * 75.88
    elif ticket == 'Premium':
        ttl = num_tickets * 125.22
    elif ticket == 'VIP':
        ttl = num_tickets * 300.4
elif stage == 'Final':
    if ticket == 'Standard':
        ttl = num_tickets * 110.1
    elif ticket == 'Premium':
        ttl = num_tickets * 160.66
    elif ticket == 'VIP':
        ttl = num_tickets * 400
photos = num_tickets * 40
if ttl > 4000:
    ttl *= 0.75
    if photo == 'Y':
        ttl = ttl
elif ttl > 2500:
    ttl *= 0.9
    if photo == 'Y':
        ttl += photos
else:
    ttl = ttl
    if photo == 'Y':
        ttl += photos
print(f'{ttl:.2f}')