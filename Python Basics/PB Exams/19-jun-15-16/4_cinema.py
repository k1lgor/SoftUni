capacity = int(input())
command = ''
ppl = 0
income = 0
while command != 'Movie time!':
    command = input()
    if command == 'Movie time!':
        print(f'There are {abs(capacity)} seats left in the cinema.')
        break
    if capacity == 0:
        print(f'The cinema is full.')
        break
    ppl = int(command)
    capacity -= ppl
    if capacity < 0:
        print(f'The cinema is full.')
        break
    price = ppl * 5
    if ppl % 3 == 0:
        price -= 5
    income += price
    price = 0

print(f'Cinema income - {income:.0f} lv.')