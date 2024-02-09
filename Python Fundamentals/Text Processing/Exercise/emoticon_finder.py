def emoji_finder(data):
    start = 0

    while start < len(data):

        if (pos := data.find(':', start)) != -1:

            print(data[pos:(pos + 2)])
            start = pos + 1
        else:
            break


emoji_finder(input())
