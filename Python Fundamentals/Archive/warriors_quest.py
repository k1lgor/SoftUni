def for_Azeroth(d, c):

    while 'For Azeroth' not in c:
        c, *tok = c.split()
        if c == 'GladiatorStance':
            d = d.upper()
            print(d)
        elif c == 'DefensiveStance':
            d = d.lower()
            print(d)
        elif c == 'Dispel':
            if 0 <= int(tok[0]) < len(d):
                d = d.replace(d[int(tok[0])], tok[1], 1)
                print("Success!")
            else:
                print("Dispel too weak.")
        elif c == 'Target' and tok[0] == 'Change':
            d = d.replace(tok[1], tok[2])
            print(d)
        elif c == 'Target' and tok[0] == 'Remove':
            d = d.replace(tok[1], "")
            print(d)
        else:
            print("Command doesn't exist!")
        c = input()


data = input()
command = input()
for_Azeroth(data, command)
