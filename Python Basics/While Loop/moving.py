w = int(input())
l = int(input())
h = int(input())

room = w * l * h

while room > 0:

    if (boxes := input()) == 'Done':
        print(f'{room} Cubic meters left.')
        break

    room -= int(boxes)
if boxes != 'Done':
    print(f'No more free space! You need {abs(room)} Cubic meters more.')
