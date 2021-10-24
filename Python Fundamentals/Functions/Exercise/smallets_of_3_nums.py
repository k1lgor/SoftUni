def smallest(a, b, c):
    List.append(a)
    List.append(b)
    List.append(c)
    small = min(List)
    print(small)
    return small
List = []
smallest(a=int(input()), b=int(input()), c=int(input()))