def validator(d, c):
    while 'Complete' not in c:
        c, *tok = c.split()

        if c == 'Make' and tok[0] == 'Upper':
            d = d.replace(d[int(tok[1])], d[int(tok[1])].upper())
            print(d)
        elif c == 'Make' and tok[0] == 'Lower':
            d = d.replace(d[int(tok[1])], d[int(tok[1])].lower())
            print(d)
        elif c == 'Insert':
            if 0 <= int(tok[0]) < len(d):
                d = d[:int(tok[0])] + tok[1] + d[int(tok[0]):]
                print(d)
        elif c == 'Replace':
            if tok[0] in d:
                asci_sum = int(tok[1]) + ord(tok[0])
                d = d.replace(tok[0], chr(asci_sum))
                print(d)
        elif c == 'Validation':
            if len(d) >= 8:
                
            else:
                print("Password must be at least 8 characters long!")
        c = input()


data = input()
command = input()
validator(data, command)
