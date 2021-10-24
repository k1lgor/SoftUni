product = input()
city = input()
qnty = float(input())
sum = 0.0
if city == 'Sofia':
    if product == 'coffee':
        sum = qnty * 0.5
    elif product == 'water':
        sum = qnty * 0.8
    elif product == 'beer':
        sum = qnty * 1.2
    elif product == 'sweets':
        sum = qnty * 1.45
    elif product == 'peanuts':
        sum = qnty * 1.6
elif city == 'Plovdiv':
    if product == 'coffee':
        sum = qnty * 0.4
    elif product == 'water':
        sum = qnty * 0.7
    elif product == 'beer':
        sum = qnty * 1.15
    elif product == 'sweets':
        sum = qnty * 1.3
    elif product == 'peanuts':
        sum = qnty * 1.5
elif city == 'Varna':
    if product == 'coffee':
        sum = qnty * 0.45
    elif product == 'water':
        sum = qnty * 0.7
    elif product == 'beer':
        sum = qnty * 1.1
    elif product == 'sweets':
        sum = qnty * 1.35
    elif product == 'peanuts':
        sum = qnty * 1.55
print(sum)
