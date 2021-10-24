budget = float(input())
nights = int(input())
night_price = float(input())
other_exp = int(input())

percent = budget * other_exp / 100
ttl_nights = night_price * nights
if nights > 7:
    ttl_nights *= 0.95
budget -= percent + ttl_nights

if budget < 0:
    print(f'{abs(budget):.2f} leva needed.')
else:
    print(f'Ivanovi will be left with {abs(budget):.2f} leva after vacation.')
