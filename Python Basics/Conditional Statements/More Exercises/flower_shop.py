import math
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactuses = int(input())
gift = float(input())

ttl = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cactuses * 8
ttl *= 0.95

if ttl >= gift:
    print(f'She is left with {math.floor(abs(ttl - gift))} leva.')
else:
    print(f'She will have to borrow {math.ceil(abs(ttl - gift))} leva.')
