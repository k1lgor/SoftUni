def multiSign():

    if 0 in LIST:
        return print('zero')
    counter = sum(i > 0 for i in LIST)
    if counter % 2 == 0:
        print('negative')
    else:
        print('positive')


LIST = []

n1, n2, n3 = LIST.append(int(input())), LIST.append(
    int(input())), LIST.append(int(input()))
multiSign()
