len_1, len_2 = input().split()

set1 = {int(input()) for x in range(int(len_1))}
set2 = {int(input()) for y in range(int(len_2))}

[print(x) for x in set1.intersection(set2)]
