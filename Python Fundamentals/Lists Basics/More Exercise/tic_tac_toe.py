line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

win = False
winner = ''
while True:
    if line1[0] == 1 and line2[0] == 1 and line3[0] == 1:
        win = True
        winner = 'First'
    elif line1[1] == 1 and line2[1] == 1 and line3[1] == 1: 
        win = True
        winner = 'First'
    elif line1[2] == 1 and line2[2] == 1 and line3[2] == 1:
        win = True
        winner = 'First'
    elif line1[0] == 1 and line2[1] == 1 and line3[2] == 1:
        win = True
        winner = 'First'
    elif line1[2] == 1 and line2[1] == 1 and line3[0] == 1:
        win = True
        winner = 'First'
    elif line1[0] == 1 and line1[1] == 1 and line1[2] == 1:
        win = True
        winner = 'First'
    elif line2[0] == 1 and line2[1] == 1 and line2[2] == 1:
        win = True
        winner = 'First'
    elif line3[0] == 1 and line3[1] == 1 and line3[2] == 1:
        win = True
        winner = 'First'
    elif line1[0] == 2 and line2[0] == 2 and line3[0] == 2:
        win = True
        winner = 'Second'
    elif line1[1] == 2 and line2[1] == 2 and line3[1] == 2: 
        win = True
        winner = 'First'
    elif line1[2] == 2 and line2[2] == 2 and line3[2] == 2:
        win = True
        winner = 'Second'
    elif line1[0] == 2 and line2[1] == 2 and line3[2] == 2:
        win = True
        winner = 'Second'
    elif line1[2] == 2 and line2[1] == 2 and line3[0] == 2:
        win = True
        winner = 'Second'
    elif line1[0] == 2 and line1[1] == 2 and line1[2] == 2:
        win = True
        winner = 'Second'
    elif line2[0] == 2 and line2[1] == 2 and line2[2] == 2:
        win = True
        winner = 'Second'
    elif line3[0] == 2 and line3[1] == 2 and line3[2] == 2:
        win = True
        winner = 'Second'
    else:
        print('Draw!')
        break
        
    if win:
        print(f'{winner} player won')
        break