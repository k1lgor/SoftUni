import math
hrs = int(input())
days = int(input())
workers = int(input())

ttl_hrs = days * 0.9 * 8
overtime = workers * 2 * days
ttl = math.floor(ttl_hrs + overtime)
if ttl >= hrs:
    print(f'Yes!{abs(ttl - hrs):.0f} hours left.')
else:
    print(f'Not enough time!{abs(ttl - hrs):.0f} hours needed.')
