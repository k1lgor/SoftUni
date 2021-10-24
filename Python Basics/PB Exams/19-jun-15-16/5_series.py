budget = float(input())
serials = int(input())
title = ''
price = 0
ttl = 0
for i in range(serials):
    title = input()
    price = float(input())

    if title == 'Thrones':
        ttl += price * 0.5
    elif title == 'Lucifer':
        ttl += price * 0.6
    elif title == 'Protector':
        ttl += price * 0.7
    elif title == 'TotalDrama':
        ttl += price * 0.8
    elif title == 'Area':
        ttl += price * 0.9
    else:
        ttl += price
if budget < ttl:
    print(f'You need {abs(budget - ttl):.2f} lv. more to buy the series!')
else:
    print(f'You bought all the series and left with {abs(budget - ttl):.2f} lv.')

