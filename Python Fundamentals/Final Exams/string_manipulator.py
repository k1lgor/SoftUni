def manipulator(d, c):
    while 'End' not in c:
        c, *tok = c.split()
        if c == 'Translate':
            d = d.replace(tok[0], tok[1])
            print(d)
        elif c == 'Includes':
            if tok[0] in d:
                print("True")
            else:
                print("False")
        elif c == 'Start':
            if d.startswith(tok[0]):
                print("True")
            else:
                print("False")
        elif c == 'Lowercase':
            d = d.lower()
            print(d)
        elif c == 'FindIndex':
            index = d.rfind(tok[0])
            print(index)
        elif c == 'Remove':
            d = d.replace(d[int(tok[0]):int(tok[0])+int(tok[1])], "")
            print(d)
        c = input()


data = input()
command = input()
manipulator(data, command)
