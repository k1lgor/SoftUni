def emoji_finder(data):
    start = 0

    while start < len(data):

        pos = data.find(':', start)
        if pos != -1:

            print(data[pos:(pos + 2)])
            start = pos + 1
        else:
            break


emoji_finder(input())
