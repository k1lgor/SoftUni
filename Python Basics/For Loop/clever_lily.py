n = int(input())
laundry = float(input())
toy = int(input())
gift = 0
money = 0
ttl = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        money += 10
        ttl += money - 1
    else:
        gift += 1

ttl += gift * toy
if ttl >= laundry:
    print(f'Yes! {abs(ttl - laundry):.2f}')
else:
    print(f'No! {abs(ttl - laundry):.2f}')
