fruit = input()
packet = input()
sets = int(input())

if packet == 'small':
    if fruit == 'Watermelon':
        price = 56 * 2
    elif fruit == 'Mango':
        price = 36.66 * 2
    elif fruit == 'Pineapple':
        price = 42.1 * 2
    elif fruit == 'Raspberry':
        price = 20 * 2
elif packet == 'big':
    if fruit == 'Watermelon':
        price = 28.7 * 5
    elif fruit == 'Mango':
        price = 19.6 * 5
    elif fruit == 'Pineapple':
        price = 24.8 * 5
    elif fruit == 'Raspberry':
        price = 15.2 * 5
ttl = sets * price
if 400 <= ttl <= 1000:
    ttl *= 0.85
elif ttl > 1000:
    ttl /= 2
print(f'{ttl:.2f} lv.')