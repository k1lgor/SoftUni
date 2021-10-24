from math import floor
n = int(input())
color = ''
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
for i in range(n):
    color = input()
    if color == 'red':
        points += 5
        red += 1
    elif color == 'orange':
        points += 10
        orange += 1
    elif color == 'yellow':
        points += 15
        yellow += 1
    elif color == 'white':
        points += 20
        white += 1
    elif color == 'black':
        points /= 2
        black += 1
    else:
        other += 1

print(f'Total points: {floor(points)}')
print(f'Points from red balls: {red}')
print(f'Points from orange balls: {orange}')
print(f'Points from yellow balls: {yellow}')
print(f'Points from white balls: {white}')
print(f'Other colors picked: {other}')
print(f'Divides from black balls: {black}')