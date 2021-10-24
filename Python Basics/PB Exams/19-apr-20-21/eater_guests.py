from math import ceil
guests = int(input())
budget = int(input())

bread = ceil(guests / 3)
eggs = guests * 2
ttl_bread = bread * 4
ttl_eggs = eggs * 0.45

ttl = ttl_bread + ttl_eggs

if ttl > budget:
    print(f'Lyubo doesn\'t have enough money.\nHe needs {abs(ttl - budget):.2f} lv. more.')
else:
    print(f'Lyubo bought {bread} Easter bread and {eggs} eggs.\nHe has {abs(ttl - budget):.2f} lv. left.')