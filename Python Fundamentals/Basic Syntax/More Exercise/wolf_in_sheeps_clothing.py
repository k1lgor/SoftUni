text = input()
curr_list = list(text.split(', '))

if curr_list.pop() == 'wolf':
    print('Please go away and stop eating my sheep')

else:
    curr_list.reverse()
    for x in range(len(curr_list)):
        if curr_list[x] != 'sheep':
            print(
                f'Oi! Sheep number {x + 1}! You are about to be eaten by a wolf!')
