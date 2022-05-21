string = list(input())
command = input()
letter_sum = 0

if command == 'LOWERCASE':
    for i in string[::]:
        if i.islower():
            letter_sum += ord(i)

elif command == 'UPPERCASE':
    for i in string[::]:
        if i.isupper():
            letter_sum += ord(i)
print(f'The total sum is: {letter_sum}')
