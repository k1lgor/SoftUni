film = input()
packet = input()
tickets = int(input())

if film == 'John Wick':
    if packet == 'Drink':
        ttl = tickets * 12
    elif packet == 'Popcorn':
        ttl = tickets * 15
    elif packet == 'Menu':
        ttl = tickets * 19
elif film == 'Star Wars':
    if packet == 'Drink':
        ttl = tickets * 18
    elif packet == 'Popcorn':
        ttl = tickets * 25
    elif packet == 'Menu':
        ttl = tickets * 30
    if tickets >= 4:
        ttl *= 0.7
elif film == 'Jumanji':
    if packet == 'Drink':
        ttl = tickets * 9
    elif packet == 'Popcorn':
        ttl = tickets * 11
    elif packet == 'Menu':
        ttl = tickets * 14
    if tickets == 2:
        ttl *= 0.85
print(f'Your bill is {ttl:.2f} leva.')