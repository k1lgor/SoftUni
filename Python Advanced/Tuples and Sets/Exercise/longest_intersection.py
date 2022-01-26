num = int(input())


def find_inter(fs, fe, ss, se, z):
    n1 = set(range(int(fs), int(fe) + 1))
    n2 = set(range(int(ss), int(se) + 1))

    return z.append(n1.intersection(n2))


inter = []
for _ in range(num):
    first, second = input().split('-')
    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')
    find_inter(first_start, first_end, second_start, second_end, inter)

max_len = ""
for i in inter:
    if len(i) > len(max_len):
        max_len = i
print(f"Longest intersection is {[x for x in max_len]} with length {len(max_len)}")
