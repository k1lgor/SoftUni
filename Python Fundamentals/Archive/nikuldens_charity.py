def charity(d, c,):

    while 'Finish' not in c:
        c, *tok = c.split()
        if c == 'Replace':
            d = d.replace(tok[0], tok[1])
            print(d)
        elif c == 'Cut':
            if 0 <= int(tok[0]) < len(d) and 0 <= int(tok[1]) < len(d):
                d = d[:int(tok[0])] + d[int(tok[1]) + 1:]
                print(d)
            else:
                print("Invalid indexes!")
        elif c == 'Make' and tok[0] == 'Upper':
            d = d.upper()
            print(d)
        elif c == 'Make' and tok[0] == 'Lower':
            d = d.lower()
            print(d)
        elif c == 'Check':
            if tok[0] in d:
                print(f"Message contains {tok[0]}")
            else:
                print(f"Message doesn't contain {tok[0]}")
        elif c == 'Sum':
            if 0 <= int(tok[0]) < len(d) and 0 <= int(tok[1]) < len(d):
                print(sum(ord(x) for x in d[int(tok[0]):int(tok[1]) + 1]))
            else:
                print("Invalid indexes!")
        c = input()


data = input()
command = input()
charity(data, command)
