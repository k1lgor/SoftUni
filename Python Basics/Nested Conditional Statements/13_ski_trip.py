day = int(input())
room = input()
evaluation = input()
discount = 0.0
ttl = 0.0
days = day - 1
if room == 'room for one person':
    ttl = days * 18
    discount = ttl
elif room == 'apartment':
    ttl = days * 25
    if days < 10:
        discount = ttl * 0.7
    elif 10 <= days < 15:
        discount = ttl * 0.65
    else:
        discount = ttl * 0.5
elif room == 'president apartment':
    ttl = days * 35
    if days < 10:
        discount = ttl * 0.9
    elif 10 <= days < 15:
        discount = ttl * 0.85
    else:
        discount = ttl * 0.8

if evaluation == 'positive':
    discount += discount * 0.25
else:
    discount *= 0.9

print(f'{discount:.2f}')
