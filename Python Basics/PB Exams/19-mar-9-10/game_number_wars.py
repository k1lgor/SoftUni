name1 = input()
name2 = input()

card = ''
card1 = 0
card2 = 0
points1 = 0
points2 = 0
while card1 != 'End of game':
    card = input()
    if card == 'End of game':
        print(f'{name1} has {points1} points')
        print(f'{name2} has {points2} points')
        break

    card1 = int(card)
    card2 = int(input())
    if card1 > card2:
        points1 += card1 - card2
    elif card1 < card2:
        points2 += card2 - card1
    elif card1 == card2:
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            print(f'Number wars!\n{name1} is winner with {points1} points')
            break
        elif card1 < card2:
            print(f'Number wars!\n{name2} is winner with {points2} points')
            break

