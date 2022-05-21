from math import sqrt, floor


def centerPoint():
    first = sqrt((pow(x1, 2)) + (pow(y1, 2)))
    second = sqrt((pow(x2, 2)) + (pow(y2, 2)))
    line_1 = first + second

    third = sqrt((pow(x3, 2)) + (pow(y3, 2)))
    fourth = sqrt((pow(x4, 2)) + (pow(y4, 2)))
    line_2 = third + fourth

    if line_1 >= line_2:
        if first <= second:
            print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
        else:
            print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
    elif third <= fourth:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input())

centerPoint()
