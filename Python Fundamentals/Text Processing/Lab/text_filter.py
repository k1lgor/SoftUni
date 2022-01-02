def filter(ban_list, text):
    start = 0
    while start < len(text):

        for i in ban_list:
            pos = text.find(i, start)

            if pos != -1:
                start = pos + 1
                text = text.replace(i, ('*' * len(i)))
            continue
        break
    print(text)


filter(input().split(', '), input())
