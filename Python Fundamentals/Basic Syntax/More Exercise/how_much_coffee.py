command = ''
coffee = 0

ma_list = ['coding', 'CODING', 'DOG', 'CAT', 'MOVIE', 'dog', 'cat', 'movie']

while command != 'END':
    if coffee >= 5:
        print('You need extra sleep')
        exit()
    if command in ma_list:
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2
    command = input()

print(coffee)
