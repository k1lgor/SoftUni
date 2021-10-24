minutes = int(input())
seconds = int(input())
length = float(input())
secs_100m = int(input())
delay = 2.5

control = minutes * 60 + seconds
delay_time = length / 120
ttl_delay = delay_time * delay
time = (length / 100) * secs_100m - ttl_delay

if time > control:
    print(f'No, Marin failed! He was {abs(time - control):.3f} second slower.')
else:
    print(f'Marin Bangiev won an Olympic quota!\nHis time is {time:.3f}.')