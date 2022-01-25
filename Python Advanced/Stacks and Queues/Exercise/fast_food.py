from collections import deque

ttl_food = int(input())
order = deque(int(x) for x in input().split(' '))
print(max(order))

while order:
    customer = order[0]
    if ttl_food < customer:
        break
    ttl_food -= customer
    order.popleft()

if not order:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in order)}")
