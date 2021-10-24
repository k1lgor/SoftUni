x = float(input())
y = float(input())
h = float(input())

nl = '\n'

back_wall = x ** 2
front_wall = (x ** 2) - (1.2 * 2)
side_wall = ((x * y) * 2) - ((1.5 ** 2) * 2)
roof1 = x * y * 2
roof2 = (x * h / 2) * 2

print(f'{((back_wall + front_wall + side_wall) / 3.4): .2f}{nl}{((roof1 + roof2) / 4.3): .2f}')
