eggs1 = int(input())
eggs2 = int(input())
winner = ''

while winner != 'End of battle':
    if eggs1 == 0:
        print(f'Player one is out of eggs. Player two has {eggs2} eggs left.')
        break
    if eggs2 == 0:
        print(f'Player two is out of eggs. Player one has {eggs1} eggs left.')
        break
    winner = input()
    if winner == 'End of battle':
        print(f'Player one has {eggs1} eggs left.\nPlayer two has {eggs2} eggs left.')
        break

    if winner == 'one':
        eggs2 -= 1
    elif winner == 'two':
        eggs1 -= 1
