vac_money = float(input())
cur_money = float(input())
spendsave = ''
money = 0
counter_spend = 0
days = 0
while cur_money <= vac_money:
    spendsave = input()
    money = float(input())
    if spendsave == 'spend':
        counter_spend += 1
        cur_money -= money
        cur_money = max(cur_money, 0)
    else:
        cur_money += money
        counter_spend = 0
    days += 1
    if cur_money >= vac_money:
        print(f'You saved the money for {days} days.')
        break
    if counter_spend >= 5:
        print(f'You can\'t save the money.\n{days}')
        break
