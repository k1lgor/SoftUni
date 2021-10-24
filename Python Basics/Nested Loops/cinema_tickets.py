movie_name = input()
free_seats = 0
tickets = 0
student = 0
standard = 0
kid = 0
while movie_name != 'Finish':
    ticket = ''
    student_counter = 0
    standard_counter = 0
    kid_counter = 0
    ttl_tickets = 0
    free_seats = int(input())
    while ticket != 'End':
        if ttl_tickets == free_seats:
            break
        ticket = input()
        if ticket == 'student':
            student_counter += 1
        elif ticket == 'standard':
            standard_counter += 1
        elif ticket == 'kid':
            kid_counter += 1
        ttl_tickets = student_counter + standard_counter + kid_counter
    print(f'{movie_name} - {((ttl_tickets / free_seats) * 100):.2f}% full.')

    tickets += ttl_tickets
    student += student_counter
    standard += standard_counter
    kid += kid_counter
    movie_name = input()
print(f'Total tickets: {tickets}\n{((student / tickets) * 100):.2f}% student tickets.\n{((standard / tickets) * 100):.2f}% standard tickets.\n{((kid / tickets) * 100):.2f}% kids tickets.')
