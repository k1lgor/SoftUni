from math import sqrt, floor


def centerPoint():
    first = sqrt((pow(x1, 2)) + (pow(y1, 2)))
    second = sqrt((pow(x2, 2)) + (pow(y2, 2)))

    if first <= second:
        print(f'({floor(x1)}, {floor(y1)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})')


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
centerPoint()
