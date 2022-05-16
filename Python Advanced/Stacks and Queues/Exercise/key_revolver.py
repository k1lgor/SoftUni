from collections import deque

bullet_price = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split(' ')]
locks = deque([int(x) for x in input().split(' ')])
intelligence = int(input())

ttl_bullets = 0
counter = 0

while bullets and len(locks) != 0:
    if bullets.pop() > locks[0]:
        print("Ping!")
    else:
        locks.popleft()
        print("Bang!")
    ttl_bullets += 1
    counter += 1
    if counter % barrel == 0 and bullets:
        print("Reloading!")

if len(locks) > len(bullets):
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (ttl_bullets * bullet_price)}")
