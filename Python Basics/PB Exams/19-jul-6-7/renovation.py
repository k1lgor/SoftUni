from math import ceil as c
h = int(input())
w = int(input())
not_painted = int(input())
command = input()
paint = 0
walls = 4
ttl = 0
cm = c(h * w * walls * (abs(not_painted - 100) / 100))
while command != 'Tired!':
    paint = int(command)
    ttl += paint
    if ttl >= cm:
        break
    command = input()
if command == 'Tired!':
    print(f'{abs(ttl - cm):.0f} quadratic m left.')
elif ttl > cm:
    print(
        f'All walls are painted and you have {abs(ttl - cm):.0f} l paint left!')
elif cm == ttl:
    print(f'All walls are painted! Great job, Pesho!')
