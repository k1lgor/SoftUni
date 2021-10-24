start = int(input())
end = int(input())
magic = int(input())
comb = 0
flag = False
for i in range(start, end + 1):
    for j in range(start, end + 1):
        comb += 1
        if i + j == magic:
            flag = True
            print(f'Combination N:{comb} ({i} + {j} = {magic})')
            break
    if flag:
        break
    if i < j:
        continue
    print(f'{comb} combinations - neither equals {magic}')
