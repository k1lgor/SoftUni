import itertools


def jackpot(t):
    for s in symbols:
        if s in ticket and ticket.count(s) == 20:
            print(f'ticket "{ticket}" - 10{s} Jackpot!')
            return True
    return False


def win_ticket(t):
    left = ticket[:10]
    right = ticket[10:]
    for s, i in itertools.product(symbols, range(9, 5, -1)):
        if s * i in left and s * i in right:
            print(f'ticket "{ticket}" - {i}{s}')
            return True
    return False


data = [x.strip() for x in input().split(", ")]
symbols = ['@', '#', '$', '^']

for ticket in data:
    if len(ticket) == 20:
        if jackpot(ticket):
            continue
        if not win_ticket(ticket):
            print(f'ticket "{ticket}" - no match')
        continue
    else:
        print('invalid ticket')
