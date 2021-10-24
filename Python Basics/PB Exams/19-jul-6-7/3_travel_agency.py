city = input()
packet = input()
vip = input()
days = int(input())
price = 0

if days > 7:
    days -= 1

if city in ['Bansko', 'Borovets'] and packet in ['noEquipment', 'withEquipment']:
    if packet == 'noEquipment':
        price = days * 80
        if vip == 'yes':
            price *= 0.95

    elif packet == 'withEquipment':
        price = days * 100
        if vip == 'yes':
            price *= 0.9

    else:
        print('Invalid input!')
    if days < 1:
        print('Days must be positive number!')
    else:
        print(f'The price is {price:.2f}lv! Have a nice time!')

elif city in ['Varna', 'Burgas'] and packet in ['noBreakfast', 'withBreakfast']:
    if packet == 'noBreakfast':
        price = days * 100
        if vip == 'yes':
            price *= 0.93

    elif packet == 'withBreakfast':
        price = days * 130
        if vip == 'yes':
            price *= 0.88
        0
    else:
        print('Invalid input!')
    if days < 1:
        print('Days must be positive number!')
    else:
        print(f'The price is {price:.2f}lv! Have a nice time!')
else:
    print('Invalid input!')
