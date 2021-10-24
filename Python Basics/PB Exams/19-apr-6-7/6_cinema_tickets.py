name_movie = input()

ticket = ''
student = 0
standard = 0
kid = 0
ttl_tickets = 0
tickets = 0
while name_movie != 'Finish':
    if name_movie == 'Finish':
        break
    free_seats = int(input())
    for i in range(free_seats):
        ticket = input()
        if ticket == 'End':
            break
        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        elif ticket == 'kid':
            kid += 1
        tickets += 1

    print(f'{name_movie} - {(tickets / free_seats) * 100:.2f}% full.')
    ttl_tickets += tickets

    tickets = 0
    name_movie = input()

print(f'Total tickets: {ttl_tickets}')
print(f'{(student / ttl_tickets) * 100:.2f}% student tickets.')
print(f'{(standard / ttl_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid / ttl_tickets) * 100:.2f}% kids tickets.')
