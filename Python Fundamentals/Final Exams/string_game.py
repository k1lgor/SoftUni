def game(d, c):
    while 'Done' not in c:
        c, *tokens = c.split()
        if c == 'Change':
            d = d.replace(tokens[0], tokens[1])
            print(d)
        elif c == 'Includes':
            if tokens[0] in d:
                print("True")
            else:
                print("False")
        elif c == 'End':
            len_end = len(tokens[0])
            end_d = d[-len_end:]
            if end_d == tokens[0]:
                print("True")
            else:
                print("False")
        elif c == 'Uppercase':
            d = d.upper()
            print(d)
        elif c == 'FindIndex':
            index = d.find(tokens[0])
            print(index)
        elif c == 'Cut':
            cut = d[int(tokens[0]):int(tokens[0])+int(tokens[1])]
            print(cut)

        c = input()


data = input()
command = input()
game(data, command)
