gifts = input().split(' ')

command = input().split(' ')

while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]
        gifts = ' '.join(map(str, gifts))
        gifts = gifts.replace(gift, 'None')
        gifts = gifts.split(' ')
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    
    command = input().split(' ')
    
while 'None' in gifts:
    gifts.remove('None')
    
print(' '.join(map(str, gifts)))
