city = input()
packet = input()
vip = input()
days = int(input())

if days > 7:
    days -= 1

if not (city in ['Bansko', 'Borovets'] and packet in ['noEquipment', 'withEquipment']) and not (city in ['Varna', 'Burgas'] and packet in \
['noBreakfast', 'withBreakfast']):
    print('Invalid input!')

elif days < 1:
    print('Days must be positive number!')

else:
    if city in ['Bansko', 'Borovets']:
        if packet == 'noEquipment':
            ttl = days * 80
            if vip == 'yes':
                ttl *= 0.95
        elif packet == 'withEquipment':
            ttl = days * 100
            if vip == 'yes':
                ttl *= 0.9
    elif city in ['Varna', 'Burgas']:
        if packet == 'noBreakfast':
            ttl = days * 100
            if vip == 'yes':
                ttl *= 0.93
        elif packet == 'withBreakfast':
            ttl = days * 130
            if vip == 'yes':
                ttl *= 0.88

    print(f'The price is {ttl:.2f}lv! Have a nice time!')