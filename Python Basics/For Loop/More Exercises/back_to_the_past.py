inheritage = float(input())
year = int(input())
for yold, i in enumerate(range(1800, year + 1), start=18):
    inheritage -= 12000 if i % 2 == 0 else 12000 + 50 * yold
if inheritage < 0:
    print(f'He will need {abs(inheritage):.2f} dollars to survive.')
else:
    print(
        f'Yes! He will live a carefree life and will have {inheritage:.2f} dollars left.')
