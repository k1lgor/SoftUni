tournaments = ''
games = 0
won = 0
lost = 0
counter = 0
while tournaments != 'End of tournaments':
    tournaments = input()
    if tournaments == 'End of tournaments':
        break
    games = int(input())
    points1 = 0
    points2 = 0
    for i in range(1, games + 1):
        points1 = int(input())
        points2 = int(input())
        if points1 > points2:
            print(
                f'Game {i} of tournament {tournaments}: win with {abs(points1 - points2)} points.')
            won += 1
        elif points2 > points1:
            print(
                f'Game {i} of tournament {tournaments}: lost with {abs(points1 - points2)} points.')
            lost += 1
    counter += games
print(f'{(won / counter) * 100:.2f}% matches win')
print(f'{(lost / counter) * 100:.2f}% matches lost')
