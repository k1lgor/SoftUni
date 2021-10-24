team = input()
games = int(input())
w = 0
d = 0
l = 0
points = 0
result = ''
if games == 0:
    print(f'{team} hasn\'t played any games during this season.')
else:
    for _ in range(games):
        result = input()
        if result == 'D':
            d += 1
            points += 1
        elif result == 'L':
            l += 1
        elif result == 'W':
            w += 1
            points += 3
    print(f'{team} has won {points} points during this season.\nTotal stats:\n## W: {w}\n## D: {d}\n## L: {l}\nWin rate: {(w / games) * 100:.2f}%')
