data = input()
players = {}
total = {}
deleted = False
while data != 'Season end':
    split_data = data.split(" -> ")
    if len(split_data) > 1:
        player, pos, skill = data.split(" -> ")
        skill = int(skill)
        if player in players:
            if pos in players[player]:
                players[player][pos] = max(players[player][pos], skill)
            else:
                players[player][pos] = skill
        else:
            players[player] = {pos: skill}
    else:
        p1, p2 = data.split(" vs ")
        if p1 in players and p2 in players:
            for k1 in players[p1].keys():
                for k2 in players[p2].keys():
                    if k1 == k2:
                        if sum(players[p1].values()) > sum(players[p2].values()):
                            del players[p2]
                        elif sum(players[p1].values()) < sum(players[p2].values()):
                            del players[p1]
                        deleted = True
                        break
                if deleted:
                    break
    data = input()

for playa, skillz in players.items():
    if playa not in total:
        total[playa] = 0
    for s in skillz.values():
        total[playa] += s

for user, points in sorted(total.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{user}: {points} skill")
    for position, skills in sorted(players[user].items(), key=lambda kvp: -kvp[1]):
        print(f"- {position} <::> {skills}")
