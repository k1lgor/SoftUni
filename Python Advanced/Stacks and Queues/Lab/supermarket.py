data = input()
names = []

while 'End' not in data:

    if data == 'Paid':
        print(*names, sep='\n')
        names.clear()
    else:
        names.append(data)

    data = input()

print(f"{len(names)} people remaining.")
