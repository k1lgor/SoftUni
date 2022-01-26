from collections import deque


def conv_time(t):
    h, m, s = [int(x) for x in t.split(":")]
    return h * 3600 + m * 60 + s


def conv_sec(s):
    s %= 24 * 60 * 60
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return f"{h:02d}:{m:02d}:{s:02d}"


data = input().split(";")
time = conv_time(input())
process_time = {}
busy_time = {}
items = deque()
product = input()

for i in data:
    name, t = i.split("-")
    process_time[name] = int(t)
    busy_time[name] = -1

while 'End' not in product:
    items.append(product)
    product = input()

while items:
    time += 1
    item = items.popleft()
    for k, v in busy_time.items():
        if time >= v:
            busy_time[k] = time + process_time[k]
            print(f"{k} - {item} [{conv_sec(time)}]")
            break
    else:
        items.append(item)
