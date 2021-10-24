price_over_20 = float(input())
kg_baggage = float(input())
days = int(input())
baggages = int(input())

if kg_baggage < 10:
    price = price_over_20 * 0.2
elif 10 <= kg_baggage <= 20:
    price = price_over_20 / 2
elif kg_baggage > 20:
    price = price_over_20
if days > 30:
    price *= 1.1
elif 7 <= days <= 30:
    price *= 1.15
elif days < 7:
    price *= 1.4
ttl = baggages * price
print(f'The total price of bags is: {ttl:.2f} lv.')