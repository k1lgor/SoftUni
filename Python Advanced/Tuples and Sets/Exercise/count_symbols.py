occurrence = {}
for char in input():
    if char not in occurrence:
        occurrence[char] = 1
    else:
        occurrence[char] += 1

for k, v in sorted(occurrence.items()):
    print(f"{k}: {v} time/s")
