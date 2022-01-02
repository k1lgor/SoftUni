def chars(data):
    result = ""
    last_letter = ""

    for i in data:
        if i in result and last_letter != i or last_letter != i:
            result += i
        last_letter = i
    print(result)


chars(input())
