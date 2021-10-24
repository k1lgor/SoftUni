from math import floor as fl
from math import ceil as cl
rocket = float(input())
nums_rocket = int(input())
nums_snickers = int(input())

ttl_rocket = rocket * nums_rocket
snickers = rocket / 6
ttl_snickers = snickers * nums_snickers
others = (ttl_rocket + ttl_snickers) * 0.2

grant_ttl = ttl_rocket + ttl_snickers + others
print(f'Price to be paid by Djokovic {fl(grant_ttl / 8)}')
print(f'Price to be paid by sponsors {cl(grant_ttl * 7 / 8)}')
