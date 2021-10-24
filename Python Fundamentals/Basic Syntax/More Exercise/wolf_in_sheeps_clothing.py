text = input()
list = list(text.split(', '))

if list.pop() == 'wolf':
    print('Please go away and stop eating my sheep')

else:
    list.reverse()
    for x in range(len(list)):
        if list[x] != 'sheep':
            print(
                f'Oi! Sheep number {x + 1}! You are about to be eaten by a wolf!')
