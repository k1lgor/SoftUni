def count(string, substring):
    counter = 0
    start = 0

    while start < len(string):

        pos = string.find(substring, start)

        if pos != -1:
            start = pos + 1
            counter += 1
        else:
            break
    print(counter)


count(input().lower(), input().lower())
