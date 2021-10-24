def validChecker():
    is_valid = True
    counter = 0
    if len(psswd) not in range(6, 11):
        print('Password must be between 6 and 10 characters')
        is_valid = False
        
    for element in psswd[::]:
        if element.isalpha() or element.isdigit():
            if element.isdigit():
                counter += 1
            continue
        else:
            print('Password must consist only of letters and digits')
            is_valid = False
            break

    if counter < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')
        
psswd = input()
validChecker()



