size = input()
color = input()
batch = int(input())
price = 0
if size == 'Large':
    if color == 'Red':
        price = 16
    elif color == 'Green':
        price = 12
    elif color == 'Yellow':
        price = 9
elif size == 'Medium':
    if color == 'Red':
        price = 13
    elif color == 'Green':
        price = 9
    elif color == 'Yellow':
        price = 7
elif size == 'Small':
    if color == 'Red':
        price = 9
    elif color == 'Green':
        price = 8
    elif color == 'Yellow':
        price = 5
ttl = price * batch
ttl *= 0.65
print(f'{ttl:.2f} leva.')