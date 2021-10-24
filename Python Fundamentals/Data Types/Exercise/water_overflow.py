cap = 255
n = int(input())
tank = 0
for _ in range(n):
    num = int(input())
    if num > cap:
        print('Insufficient capacity!')
    else:
        cap -= num
        tank += num
print(tank)