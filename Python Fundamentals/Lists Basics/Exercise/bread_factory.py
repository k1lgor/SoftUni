workingDay = input().split("|")
energy, coins = 100, 100

complete = True

for day in workingDay:
    event = day.split('-')
    name = event[0]
    num = int(event[1])

    if 'rest' in event:
        gainedEnergy = num
        if energy + gainedEnergy > 100:
            gainedEnergy = 100 - energy
            energy = 100
        else:
            energy += num
            gainedEnergy = num
        print(f'You gained {gainedEnergy} energy.\nCurrent energy: {energy}.')
    elif 'order' in event:
        if energy >= 30:
            energy -= 30
            coins += num
            print(f'You earned {num} coins.')
        else:
            energy += 50
            print('You had to rest!')
            continue
    elif coins > num:
        coins -= num
        print(f'You bought {name}.')
    else:
        print(f'Closed! Cannot afford {name}.')
        complete = False
        break

if complete:   
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')