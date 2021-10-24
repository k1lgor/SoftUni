drink = input()
sugar = input()
qnty = int(input())

if drink == 'Espresso':
    if sugar == 'Without':
        price = qnty * 0.9
    elif sugar == 'Normal':
        price = qnty * 1
    elif sugar == 'Extra':
        price = qnty * 1.2
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = qnty * 1
    elif sugar == 'Normal':
        price = qnty * 1.2
    elif sugar == 'Extra':
        price = qnty * 1.6
elif drink == 'Tea':
    if sugar == 'Without':
        price = qnty * 0.5
    elif sugar == 'Normal':
        price = qnty * 0.6
    elif sugar == 'Extra':
        price = qnty * 0.7

if sugar == 'Without':
    price *= 0.65
if drink == 'Espresso' and qnty >= 5:
    price *= 0.75
if price > 15:
    price *= 0.8
print(f'You bought {qnty} cups of {drink} for {price:.2f} lv.')
