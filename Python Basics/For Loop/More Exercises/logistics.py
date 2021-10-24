cargo = int(input())
ttl = 0
avr = 0
van = 0
truck = 0
train = 0
for _ in range(1, cargo + 1):
    tonnage = int(input())
    ttl += tonnage
    if tonnage <= 3:
        van += tonnage
    elif 4 <= tonnage <= 11:
        truck += tonnage
    elif tonnage >= 12:
        train += tonnage
avr = (van * 200 + truck * 175 + train * 120) / ttl
print(f'{avr:.2f}\n{(van / ttl * 100):.2f}%\n{(truck / ttl * 100):.2f}%\n{(train / ttl * 100):.2f}%')
