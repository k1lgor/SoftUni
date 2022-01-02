def substring(string, sub):

    while string in sub:
        sub = sub.replace(string, "")
    print(sub)


substring(input(), input())
