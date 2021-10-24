balls = int(input())
best = 0
best_w = 0
best_t = 0
best_q = 0

for _ in range(1, balls + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball = (weight / time) ** quality

    if snowball > best:
        best = int(snowball)
        best_w = weight
        best_t = time
        best_q = quality
print(f'{best_w} : {best_t} = {best} ({best_q})')