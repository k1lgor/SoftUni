price = int(input())
command = ''
counter = 1
cash = 0
paid_cash = 0
card = 0
paid_card = 0
summary = 0
while price > 0:
    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break
    if (
        counter % 2 == 0
        and int(command) < 10
        or counter % 2 != 0
        and int(command) > 100
    ):
        print('Error in transaction!')
    elif counter % 2 == 0:
        print('Product sold!')
        summary += int(command)
        card += 1
        paid_card += int(command)
    else:
        print('Product sold!')
        summary += int(command)
        cash += 1
        paid_cash += int(command)
    if summary >= price:
        print(
            f'Average CS: {(paid_cash / cash):.2f}\nAverage CC: {(paid_card / card):.2f}')
        break
    counter += 1
