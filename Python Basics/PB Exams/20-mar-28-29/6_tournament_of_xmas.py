days = int(input())
won = 0
lost = 0
ttl = 0
grand = 0
ttl_won = 0
ttl_lost = 0
for i in range(days):
    games = ''
    result = ''
    ttl = 0
    lost = 0
    won = 0
    while games != 'Finish':
        games = input()
        if games == 'Finish':
            break
        results = input()
        if results == 'win':
            won += 1
            ttl += 20
        else:
            lost += 1
    if won > lost:
        ttl *= 1.1
    grand += ttl
    ttl_won += won
    ttl_lost += lost
if ttl_won > ttl_lost:
    grand *= 1.2
    print(f'You won the tournament! Total raised money: {grand:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {grand:.2f}')