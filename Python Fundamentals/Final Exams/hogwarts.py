def hogwarts(d, c):

    while 'Abracadabra' not in c:
        c, *tok = c.split()
        if c == 'Abjuration':
            d = d.upper()
            print(d)
        elif c == 'Necromancy':
            d = d.lower()
            print(d)
        elif c == 'Illusion':
            if 0 <= int(tok[0]) < len(d):
                d = d.replace(d[int(tok[0])], tok[1])
                print("Done")
            else:
                print("The spell was too weak.")
        elif c == 'Divination':
            if tok[0] in d:
                d = d.replace(tok[0], tok[1])
                print(d)
        elif c == 'Alteration':
            if tok[0] in d:
                d = d.replace(tok[0], "")
                print(d)
        else:
            print("The spell did not work!")

        c = input()


data = input()
command = input()
hogwarts(data, command)
