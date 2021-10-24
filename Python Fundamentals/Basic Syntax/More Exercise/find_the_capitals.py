text = input()
list = []
# list = [i for i in range(len(text)) if text[i].isupper()]

for i in range(len(text)):
    if text[i].isupper():
        list.append(i)

print(list)
