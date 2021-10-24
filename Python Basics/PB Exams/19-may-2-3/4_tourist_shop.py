budget = float(input())
product = ''
price = 0
counter = 0
ttl = 0
while True:
    product = input()
    if product == 'Stop':
        print(f'You bought {counter} products for {ttl:.2f} leva.')
        break
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price /= 2

    if price > budget:
        print(f'You don\'t have enough money!\nYou need {abs(budget - price):.2f} leva!')
        break

    budget -= price
    ttl += price