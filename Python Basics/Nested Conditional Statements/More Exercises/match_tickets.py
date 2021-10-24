budget = float(input())
category = input()
ppl = int(input())
left = 0.0

if 1 <= ppl <= 4:
    left = budget * 0.25
elif 5 <= ppl <= 9:
    left = budget * 0.4
elif 10 <= ppl <= 24:
    left = budget * 0.5
elif 25 <= ppl <= 49:
    left = budget * 0.6
elif ppl >= 50:
    left = budget * 0.75

ticket = ppl * 499.99 if category == 'VIP' else ppl * 249.99
if left >= ticket:
    print(f'Yes! You have {abs(ticket - left):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(ticket - left):.2f} leva.')
