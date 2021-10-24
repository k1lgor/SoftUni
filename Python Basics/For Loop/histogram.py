n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(1, n + 1):
    num = int(input())
    if num >= 800:
        p5 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 200 <= num <= 399:
        p2 += 1
    else:
        p1 += 1
print(f'{(p1 / n * 100):.2f}%\n{(p2 / n * 100):.2f}%\n{(p3 / n * 100):.2f}%\n{(p4 / n * 100):.2f}%\n{(p5 / n * 100):.2f}%')
