qnty_eggs = int(input())
command = ''
number = 0
sold = 0
while command != 'Close':
    command = input()
    if command == 'Close':
        print(f'Store is closed!\n{sold} eggs sold.')
        break
    number = int(input())
    if command == 'Buy':
        if number <= qnty_eggs:
            qnty_eggs -= number
            sold += number
        else:
            print(f'Not enough eggs in store!\nYou can buy only {qnty_eggs}.')
            break
    elif command == 'Fill':
        qnty_eggs += number