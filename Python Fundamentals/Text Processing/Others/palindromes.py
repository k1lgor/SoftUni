text = input().split()
string = ''
last_word = ''
for i in range(len(text) - 1, -1, -1):
    
    if last_word == text[i]:
        text.remove(text[i])
    if text[i] != text[i][::-1]:
        text.remove(text[i])
        continue
    last_word = text[i]
    
text.sort(key=str.lower)
print(', '.join(text))


