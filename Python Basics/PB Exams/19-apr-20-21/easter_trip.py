dest = input()
date = input()
nights = int(input())
price = 0

if dest == 'France':
    if date == '21-23':
        price = 30
    elif date == '24-27':
        price = 35
    elif date == '28-31':
        price = 40
elif dest == 'Italy':
    if date == '21-23':
        price = 28
    elif date == '24-27':
        price = 32
    elif date == '28-31':
        price = 39
elif dest == 'Germany':
    if date == '21-23':
        price = 32
    elif date == '24-27':
        price = 37
    elif date == '28-31':
        price = 43
ttl = nights * price

print(f'Easter trip to {dest} : {ttl:.2f} leva.')