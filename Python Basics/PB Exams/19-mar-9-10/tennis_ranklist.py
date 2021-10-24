from math import floor
tournaments = int(input())
points = int(input())

text = ''
counter = 0
points2 = 0
for i in range(tournaments):
    text = input()
    if text == 'W':
        counter += 1
        points2 += 2000
    elif text == 'F':
        points2 += 1200
    elif text == 'SF':
        points2 += 720
print(f'Final points: {points + points2}')
print(f'Average points: {floor(points2 / tournaments)}')
print(f'{(counter / tournaments) * 100:.2f}%')