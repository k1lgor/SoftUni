chat = []

while True:

    command, *args = input().split()
    if command == 'end':
        break
    if command == 'Chat':
        chat.append(args[0])
    if command == 'Delete' and args[0] in chat:
        chat.remove(args[0])
    if command == 'Edit' and args[0] in chat:
        chat.insert(chat.index(args[0]), args[1])
        chat.remove(args[0])
    if command == 'Pin' and args[0] in chat:
        chat.append(chat.pop(chat.index(args[0])))
    if command == 'Spam':
        chat.extend(iter(args))
for i in chat:
    print(i)
