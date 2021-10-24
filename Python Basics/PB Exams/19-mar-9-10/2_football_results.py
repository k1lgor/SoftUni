game1 = input()
game2 = input()
game3 = input()

win = 0
lose = 0
draw = 0

if ord(game1[0]) > ord(game1[2]):
    win += 1
elif ord(game1[0]) < ord(game1[2]):
    lose += 1
else:
    draw += 1
if ord(game2[0]) > ord(game2[2]):
    win += 1
elif ord(game2[0]) < ord(game2[2]):
    lose += 1
else:
    draw += 1
if ord(game3[0]) > ord(game3[2]):
    win += 1
elif ord(game3[0]) < ord(game3[2]):
    lose += 1
else:
    draw += 1

print(f'Team won {win} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {draw}')