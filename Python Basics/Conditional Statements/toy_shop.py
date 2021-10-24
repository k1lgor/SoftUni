import math

vac_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy = int(input())
minions = int(input())
trucks = int(input())
profit = 0.0

toys = puzzles + dolls + teddy + minions + trucks

ttl_sum = puzzles * 2.6 + dolls * 3 + teddy * 4.1 + minions * 8.2 + trucks * 2

if toys >= 50:
    ttl_sum *= 0.75
rent = ttl_sum * 0.1
profit = ttl_sum - rent
if profit >= vac_price:
    print(f"Yes! {abs(profit - vac_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(profit - vac_price):.2f} lv needed.")
