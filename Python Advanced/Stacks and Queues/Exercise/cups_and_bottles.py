from collections import deque

cups_capacity = deque([int(x) for x in input().split(' ')])
filled_bottles = [int(x) for x in input().split(' ')]

wasted_water = 0

while True:
    if not filled_bottles or not cups_capacity:
        break
    if filled_bottles[-1] >= cups_capacity[0]:
        wasted_water += filled_bottles[-1] - cups_capacity[0]
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= filled_bottles[-1]
    filled_bottles.pop()

if not filled_bottles:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
else:
    bottles = []
    while filled_bottles:
        bottles.append(filled_bottles.pop())
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
print(f"Wasted litters of water: {wasted_water}")
