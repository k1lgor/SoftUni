ban_list = input().split()
text = input()
start = 0
new_text = ''
while start < len(text):
    
    for i in ban_list:
        
        if (pos := text.find(i, start)) != -1:
            start = pos + 1
            text = text.replace(i, ('*' * len(i)))
        continue
    break
print(text)
