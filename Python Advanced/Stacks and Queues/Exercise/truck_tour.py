from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    data = [int(x) for x in input().split(" ")]
    pumps.append(data)

for x in range(n):
    tank = 0
    failed = False
    for fuel, dist in pumps:
        tank += fuel
        if dist > tank:
            failed = True
            break
        tank -= dist
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(x)
        break
