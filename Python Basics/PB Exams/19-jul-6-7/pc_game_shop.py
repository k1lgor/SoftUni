sold_games = int(input())
game = ''
game1 = 0
game2 = 0
game3 = 0
game4 = 0
counter = 0
for _ in range(sold_games):
    game = input()
    if game == 'Fornite':
        game2 += 1
    elif game == 'Hearthstone':
        game1 += 1
    elif game == 'Overwatch':
        game3 += 1
    else:
        game4 += 1

print(
    f'Hearthstone - {((game1 / sold_games) * 100):.2f}%\nFornite - {((game2 / sold_games) * 100):.2f}%\nOverwatch - {((game3 / sold_games) * 100):.2f}%\nOthers - {((game4 / sold_games) * 100):.2f}%')
