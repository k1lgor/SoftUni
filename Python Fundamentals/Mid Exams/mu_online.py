dungeon = list(map(str, input().split("|")))
HP = 100
BTC = 0
stage = 1
for room in dungeon:
    room = room.split()

    if room[0] == 'potion':
        if HP < 100:
            old_hp = HP
            HP += int(room[1])
            if HP > 100:
                room[1] = 100 - old_hp
                HP = 100
        print(f"You healed for {room[1]} hp.\nCurrent health: {HP} hp.")

    elif room[0] == 'chest':
        BTC += int(room[1])
        print(f"You found {int(room[1])} bitcoins.")

    else:
        HP -= int(room[1])
        if HP > 0:
            print(f"You slayed {room[0]}.")
        else:
            print(f"You died! Killed by {room[0]}.\nBest room: {stage}")
            break

    stage += 1
if HP > 0:
    print(f"You've made it!\nBitcoins: {BTC}\nHealth: {HP}")
