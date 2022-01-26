occurrence = {}
for num in (tuple(map(float, input().split()))):
    if num not in occurrence:
        occurrence[num] = 1
    else:
        occurrence[num] += 1

for k, v in occurrence.items():
    print(f"{k} - {v} times")
