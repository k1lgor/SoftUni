budget = float(input())
GPU = int(input())
CPU = int(input())
RAM = int(input())

gpu = GPU * 250
cpu = gpu * 0.35 * CPU
ram = gpu * 0.1 * RAM

ttl = gpu + cpu + ram
if GPU > CPU:
    ttl *= 0.85

if budget < ttl:
    print(f'Not enough money! You need {abs(budget - ttl):.2f} leva more!')
else:
    print(f'You have {abs(budget - ttl):.2f} leva left!')