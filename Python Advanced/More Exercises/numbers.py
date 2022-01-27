seq1 = {int(x) for x in input().split()}
seq2 = {int(x) for x in input().split()}
num = int(input())

for _ in range(num):
    command, param, *tokens = input().split()
    if command == 'Add':
        if param == 'First':
            [seq1.add(int(x)) for x in tokens[:]]
        else:
            [seq2.add(int(x)) for x in tokens[:]]
    elif command == 'Remove':
        if param == 'First':
            seq1 = seq1.difference([int(x) for x in tokens[:]])
        else:
            seq2 = seq2.difference([int(x) for x in tokens[:]])
    else:
        print(seq1.issubset(seq2) or seq2.issubset(seq1))
print(*sorted(seq1), sep=', ')
print(*sorted(seq2), sep=', ')
