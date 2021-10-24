n1 = float(input())

if n1 == 0:
    print('zero')
elif n1 > 0:
    if n1 < 1:
        print('small positive')
    elif n1 > 1000000:
        print('large positive')
    else:
        print('positive')
elif n1 < 0:
    if abs(n1) < 1:
        print('small negative')
    elif abs(n1) > 1000000:
        print('large negative')
    else:
        print('negative')
