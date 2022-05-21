import re


def email_validator(d, c):

    while 'Complete' not in c:
        c, *tokens = c.split()
        if c == 'Make' and tokens[0] == 'Upper':
            d = d.upper()
            print(d)
        elif c == 'Make' and tokens[0] == 'Lower':
            d = d.lower()
            print(d)
        elif c == 'GetDomain':
            print(d[-3:])
        elif c == 'GetUsername':
            if '@' in d:
                if match := re.findall(r"([a-z0-9]+)@", d, re.IGNORECASE):
                    print(''.join(match))
            else:
                print(f"The email {d} doesn't contain the @ symbol.")
        elif c == 'Replace':
            d = d.replace(tokens[0], "-")
            print(d)
        elif c == 'Encrypt':
            d = [ord(x) for x in d]
            print(*d)
        c = input()


data = input()
command = input()
email_validator(data, command)
