from collections import deque

orders = deque([int(x) for x in input().split(', ')])
capacity = [int(x) for x in input().split(', ')]
ttl_pizzas = 0
while orders and capacity:
    order = orders.popleft()
    employee = capacity.pop()
    if order > 10 or order <= 0:
        capacity.append(employee)
        continue

    if order <= employee:
        ttl_pizzas += order
        continue
    else:
        ttl_pizzas += employee
        orders.appendleft(order - employee)

if len(orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {ttl_pizzas}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
if capacity:
    print(f"Employees: {', '.join(str(x) for x in capacity)}")
