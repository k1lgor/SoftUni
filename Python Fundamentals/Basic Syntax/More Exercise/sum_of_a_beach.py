text = input()
text = text.lower()

List = ['sand', 'water', 'fish', 'sun']

counter = sum(text.count(i) for i in List if i in text)
print(counter)
