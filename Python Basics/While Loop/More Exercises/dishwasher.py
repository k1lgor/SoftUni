bottles_detergent = int(input())
detergent = 750 * bottles_detergent # ml
command = ''
plates = 0
pots = 0
counter = 0
while detergent >= 0:
    command = input()
    counter += 1
    if command == 'End':
        print(f'Detergent was enough!\n{plates} dishes and {pots} pots were washed.\nLeftover detergent {abs(detergent)} ml.')
        break
    if counter % 3 == 0:
        detergent -= (int(command) * 15)
        pots += int(command)
    else:
        detergent -= (int(command) * 5)
        plates += int(command)
    if detergent < 0:
        print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
