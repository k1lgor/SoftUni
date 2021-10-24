qnty = int(input())
typE = input()
delivery = input()
price = 0
if qnty < 10:
    print(f'Invalid order')
else:
    if typE == '90X130':
        price = 110 * qnty
        if 30 < qnty < 60:
            price *= 0.95
        elif qnty > 60:
            price *= 0.92
    elif typE == '100X150':
        price = 140 * qnty
        if 40 < qnty < 80:
            price *= 0.94
        elif qnty > 80:
            price *= 0.9
    elif typE == '130X180':
        price = 190 * qnty
        if 20 < qnty < 50:
            price *= 0.93
        elif qnty > 50:
            price *= 0.88
    elif typE == '200X300':
        price = 250 * qnty
        if 25 < qnty < 50:
            price *= 0.91
        elif qnty > 50:
            price *= 0.86
    if delivery == 'With delivery':
        price += 60
    if qnty > 99:
        price *= 0.96
    print(f'{price:.2f} BGN')