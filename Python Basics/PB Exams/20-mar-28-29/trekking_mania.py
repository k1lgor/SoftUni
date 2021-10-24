groups = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
ttl = 0
for i in range(groups):
    ppl = int(input())
    if ppl <= 5:
        g1 += ppl
    elif 6 <= ppl <= 12:
        g2 += ppl
    elif 13 <= ppl <= 25:
        g3 += ppl
    elif 26 <= ppl <= 40:
        g4 += ppl
    elif ppl >= 41:
        g5 += ppl
    ttl += ppl
print(f'{(g1 / ttl) * 100:.2f}%')
print(f'{(g2 / ttl) * 100:.2f}%')
print(f'{(g3 / ttl) * 100:.2f}%')
print(f'{(g4 / ttl) * 100:.2f}%')
print(f'{(g5 / ttl) * 100:.2f}%')