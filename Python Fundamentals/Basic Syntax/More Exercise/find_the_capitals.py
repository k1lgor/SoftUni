text = input()
list = []

for i in range(len(text)):
    if text[i].isupper():
        list.append(i)

print(list)
