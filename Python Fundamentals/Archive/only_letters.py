data = input()
start = 0

while start < len(data):
    for i in data:
        if i.isdigit():
            pos = data.find(i, start)
            if pos != -1:
                start = pos + 1
                data = data.replace(data[pos : start + 1], data[start + 1])

    break

print(data)
