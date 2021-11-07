def checker(force_temp, side_temp, user_temp):
    for z, x in force_temp.items():
        if user_temp in x:
            return force_temp
    if side_temp not in force_temp:
        force_temp[side_temp] = [user_temp]
    else:
        force_temp[side_temp].append(user_temp)
    return force_temp


def double(force_temp, side_temp, user_temp):
    for z, x in force_temp.items():
        if user_temp in x:
            force_temp[z].remove(user_temp)
            return checker(force_temp, side_temp, user_temp)
    return checker(force_temp, side_temp, user_temp)


command = input()
force = {}
side, user = "", ""

while 'Lumpawaroo' not in command:
    split_list = command.split(" | ")
    if len(split_list) > 1:
        side, user = command.split(" | ")
        force = checker(force, side, user)

    else:
        user, side = command.split(" -> ")
        force = double(force, side, user)
        print(f"{user} joins the {side} side!")

    command = input()

for k, v in sorted(force.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0])):
    if v:
        print(f"Side: {k}, Members: {len(v)}")
        for user in sorted(v):
            print(f"! {user}")
