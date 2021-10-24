items = input().split('|')
budget = float(input())
ticket = 150

dic = {
    'Clothes': 50.0,
    'Shoes': 35.0,
    'Accessories': 20.5
    }
prices = []
new_price = 0
profit = 0

for i in items:
    index = i.split('->')
    item = index[0]
    money = float(index[1])
    if (item == 'Clothes' and money > dic['Clothes']) or (item ==
        'Shoes' and money > dic['Shoes'])  or (item == 'Accessories'
        and money > dic['Accessories']):
        continue

    if budget < money:
        continue

    can_buy = item in ['Clothes', 'Shoes', 'Accessories']
    if can_buy:
        budget -= money
        prices.append(money)
        profit += money
for price in prices:
    new_price = (price * 1.4)
    budget += new_price
    profit -= new_price
    print(f'{new_price:.2f}', end=' ')
print(f'\nProfit: {abs(profit):.2f}')
if budget >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')