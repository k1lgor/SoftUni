rows, cols = [int(x) for x in input().split()]
string = input()

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            print(string[col % len(string)], end='')
    else:
        for col in range(cols - 1, -1, -1):
            print(string[col % len(string)], end='')
    if len(string) > cols:
        string = string[-(len(string) - cols):] + string[:cols]
    elif cols > len(string):
        string = string[cols - len(string):] + string[:cols - len(string)]
    print()
