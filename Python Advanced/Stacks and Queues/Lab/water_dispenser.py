from collections import deque


quantity = int(input())
names = deque()
data = input()

while 'Start' not in data:
    names.appendleft(data)

    data = input()

data = input()
while 'End' not in data:

    if data.startswith('refill'):
        _, water = data.split(' ')
        quantity += int(water)
    else:
        name = names.pop()
        if int(data) <= quantity:
            print(f"{name} got water")
            quantity -= int(data)
        else:
            print(f"{name} must wait")
    data = input()

print(f"{quantity} liters left")
