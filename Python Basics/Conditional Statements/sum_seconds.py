import math
ttl_time = int(input()) + int(input()) + int(input())

minutes = math.floor(ttl_time / 60)
seconds = ttl_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
