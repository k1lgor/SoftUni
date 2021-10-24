def ABS():
    new = []
    string = list(map(float, (input().split())))
    new = [abs(i) for i in string]
    print(new)
ABS()
