budget = float(input())
dest = input()
season = input()
days = int(input())

if season == 'Winter':
    if dest == 'Dubai':
        ttl = days * 45000
    elif dest == 'Sofia':
        ttl = days * 17000
    elif dest == 'London':
        ttl = days * 24000
elif season == 'Summer':
    if dest == 'Dubai':
        ttl = days * 40000
    elif dest == 'Sofia':
        ttl = days * 12500
    elif dest == 'London':
        ttl = days * 20250
if dest == 'Dubai':
    ttl *= 0.7
elif dest == 'Sofia':
    ttl *= 1.25
if budget < ttl:
    print(f'The director needs {abs(budget - ttl):.2f} leva more!')
else:
    print(f'The budget for the movie is enough! We have {abs(budget - ttl):.2f} leva left!')