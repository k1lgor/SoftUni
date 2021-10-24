hrs = int(input())
mins = int(input())

ttl = hrs * 60 + mins + 15

hours = ttl // 60
minutes = ttl % 60
if hours == 24:
    hours = 0
if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')