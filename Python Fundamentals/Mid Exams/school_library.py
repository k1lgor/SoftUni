books = input().split("&")

while True:
    
    command, *args = input().split(" | ")
    
    if command == 'Done':
        break
    
    if command == 'Add Book':
        if args[0] not in books:
            books.insert(0, args[0])
    if command == 'Take Book':
        while args[0] in books:
            books.remove(args[0])
    if command == 'Swap Books':
        if args[0] in books and args[1] in books:
            temp1 = books.index(args[0])
            temp2 = books.index(args[1])
            tempbook1 = books[temp1]
            tempbook2 = books[temp2]
            books[temp2] = tempbook1
            books[temp1] = tempbook2            
    if command == 'Insert Book':
        if args[0] not in books:
            books.append(args[0])
    if command == 'Check Book':
        if 0 <= int(args[0]) < len(books):
            print(books[int(args[0])])

print(*books, sep=', ')