n = int(input())

pos = []
neg = []
pos_ = 0
neg_ = 0

for _ in range(n):
    num = int(input())
    if num >= 0:
        pos.append(num)
        pos_ += 1
    else:
        neg.append(num)
        neg_ += num
print(f'{pos}\n{neg}\nCount of positives: {pos_}\nSum of negatives: {neg_}')