budget = float(input())
season = input()
dest = ""
vac = ""

if budget <= 100:
    dest = 'Bulgaria'
    if season == 'summer':
        vac = 'Camp'
        budget *= 0.3
    else:
        vac = 'Hotel'
        budget *= 0.7
elif budget <= 1000:
    dest = 'Balkans'
    if season == 'summer':
        vac = 'Camp'
        budget *= 0.4
    else:
        vac = 'Hotel'
        budget *= 0.8
else:
    dest = 'Europe'
    vac = 'Hotel'
    budget *= 0.9
print(f'Somewhere in {dest}\n{vac} - {budget:.2f}')
