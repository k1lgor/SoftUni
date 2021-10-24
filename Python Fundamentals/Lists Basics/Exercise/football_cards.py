card = input()

list_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
list_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
teams = list_A + list_B
num_A = 11
num_B = 11
card_list = card.split(' ')

for _ in range(len(teams)):
    for ele in card_list:
        if ele in list_A:
            list_A.remove(ele)
            num_A -= 1
        elif ele in list_B:
            list_B.remove(ele)
            num_B -= 1
        if num_A < 7 or num_B < 7:
            break
    break
if num_A < 7 or num_B < 7:
    print(f'Team A - {num_A}; Team B - {num_B}\nGame was terminated')
else:
    print(f'Team A - {num_A}; Team B - {num_B}')

        

