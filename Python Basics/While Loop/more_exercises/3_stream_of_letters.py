char = input()

string = ''
c_counter = False
n_counter = False
o_counter = False

while char != 'End':

    if char == 'c':
        if c_counter:
            string += char
        else:
            c_counter = True
    elif char == 'n':
        if n_counter:
            string += char
        else:
            n_counter = True
    elif char == 'o':
        if o_counter:
            string += char
        else:
            o_counter = True
    elif char.isalpha():
        string += char

    if c_counter and o_counter and n_counter:
        c_counter = False
        n_counter = False
        o_counter = False
        print(string, end = ' ')
        string = ''
    char = input()
