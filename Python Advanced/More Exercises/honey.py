from collections import deque


bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
procces = deque(input().split())

ttl_honey = 0

while bees and nectar:
    bee_value = bees.popleft()
    nectar_value = nectar.pop()
    if bee_value > nectar_value:
        bees.appendleft(bee_value)
        continue
    else:
        calculation = procces.popleft()
        if calculation == '+':
            ttl_honey += bee_value + nectar_value
        elif calculation == '-':
            ttl_honey += abs(bee_value - nectar_value)
        elif calculation == '*':
            ttl_honey += bee_value * nectar_value
        elif calculation == '/' and nectar_value > 0:
            ttl_honey += bee_value / nectar_value

print(f"Total honey made: {ttl_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
