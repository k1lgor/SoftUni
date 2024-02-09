capacity = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
for _ in range(1, fans + 1):
    if (stage := str(input())) == 'A':
        a += 1
    elif stage == 'B':
        b += 1
    elif stage == 'G':
        g += 1
    elif stage == 'V':
        v += 1
print(f'{(a / fans * 100):.2f}%\n{(b / fans * 100):.2f}%\n{(v / fans * 100):.2f}%\n{(g / fans * 100):.2f}%\n{(fans / capacity * 100):.2f}%')
