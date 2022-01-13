from collections import deque


name = deque(list(input().split(' ')))
pos = int(input())

while len(name) > 1:

    name.rotate(-pos)
    print(f"Removed {name.pop()}")

print(f"Last is {name.pop()}")
