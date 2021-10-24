from math import ceil as c
ppl = int(input())
entry = float(input())
bed_price = float(input())
umbrella_price = float(input())

entry_ttl = ppl * entry
sevenfive = c(ppl * 0.75) * bed_price
half = c(ppl / 2) * umbrella_price
print(f'{(entry_ttl + sevenfive + half):.2f} lv.')
