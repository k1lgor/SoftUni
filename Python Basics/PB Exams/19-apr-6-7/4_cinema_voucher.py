voucher = int(input())
command = ''
ticket = 0
other = 0
suma = 0
while voucher > 0:
    command = input()
    if command == 'End':
        break
    name_len = len(command)
    if name_len > 8:
        suma = ord(command[0]) + ord(command[1])
        if suma > voucher:
            break
        ticket += 1
    else:
        suma = ord(command[0])
        if suma > voucher:
            break
        other += 1
    voucher -= suma
    suma = 0
print(f'{ticket}\n{other}')