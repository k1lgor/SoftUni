from math import ceil
ppl = int(input())
entry = float(input())
deck_chair = float(input())
umbrella = float(input())

ttl_tax = ppl * entry
deck_chair_ppl = ceil(ppl * 0.75) * deck_chair
umbrella_ppl = ceil(ppl / 2) * umbrella

print(f'{(ttl_tax + deck_chair_ppl + umbrella_ppl):.2f} lv.')