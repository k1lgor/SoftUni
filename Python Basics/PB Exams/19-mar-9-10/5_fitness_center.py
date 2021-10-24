visitors = int(input())
text = ''
back = 0
chest = 0
legs = 0
ABS = 0
shake = 0
bar = 0


for i in range(visitors):
    text = input()
    if text == 'Back':
        back += 1
    elif text == 'Chest':
        chest += 1
    elif text == 'Legs':
        legs += 1
    elif text == 'Abs':
        ABS += 1
    elif text == 'Protein shake':
        shake += 1
    elif text == 'Protein bar':
        bar += 1

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{ABS} - abs')
print(f'{shake} - protein shake')
print(f'{bar} - protein bar')
print(f'{((back + chest + legs + ABS) / visitors) * 100:.2f}% - work out')
print(f'{((shake + bar) / visitors) * 100:.2f}% - protein')
