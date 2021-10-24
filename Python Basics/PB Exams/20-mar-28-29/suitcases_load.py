capacity = float(input())
command = ''
vol = 0
baggage = 0
while command != 'End':
    command = input()
    if command == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break
    vol = float(command)
    baggage += 1
    if baggage % 3 == 0:
        vol *= 1.1
    if vol >= capacity:
        if vol == capacity:
            print(f'No more space!')
            break
        else:
            baggage -= 1
            print(f'No more space!')
            break

    capacity -= vol
print(f'Statistic: {baggage} suitcases loaded.')