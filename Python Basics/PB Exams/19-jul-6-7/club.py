wanted_money = float(input())
cocktail = ''
num_cocktails = 0
ttl = 0
single_order = 0
while cocktail != 'Party!':
    if ttl >= wanted_money:
        print(f'Target acquired.')
        break
    cocktail = input()
    if cocktail == 'Party!':
        print(f'We need {abs(wanted_money - ttl):.2f} leva more.')
        break
    num_cocktails = int(input())
    cocktail_price = int(len(cocktail))
    single_order = cocktail_price * num_cocktails
    if single_order % 2 != 0:
        single_order *= 0.75
    ttl += single_order

print(f'Club income - {ttl:.2f} leva.')
