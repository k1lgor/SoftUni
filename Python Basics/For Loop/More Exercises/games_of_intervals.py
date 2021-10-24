moves = int(input())
points = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
for _ in range(1, moves + 1):
    num = int(input())
    if num > 50 or num < 0:
        n6 += 1
        points /= 2
    if 0 <= num <= 9:
        n1 += 1
        points += num * 0.2
    if 10 <= num <= 19:
        n2 += 1
        points += num * 0.3
    if 20 <= num <= 29:
        n3 += 1
        points += num * 0.4
    if 30 <= num <= 39:
        n4 += 1
        points += 50
    if 40 <= num <= 50:
        n5 += 1
        points += 100
print(f'{points:.2f}\nFrom 0 to 9: {(n1 / moves * 100):.2f}%\nFrom 10 to 19: {(n2 / moves * 100):.2f}%\nFrom 20 to 29: {(n3 / moves * 100):.2f}%\nFrom 30 to 39: {(n4 / moves * 100):.2f}%\nFrom 40 to 50: {(n5 / moves * 100):.2f}%\nInvalid numbers: {(n6 / moves * 100):.2f}%')
