def null_checker(curr_data):
    drake, name_drake, dmg_drake, hp_drake, ar_drake = curr_data.split()
    if dmg_drake == "null":
        dmg_drake = 45
    if hp_drake == "null":
        hp_drake = 250
    if ar_drake == "null":
        ar_drake = 10
    return drake, name_drake, int(dmg_drake), int(hp_drake), int(ar_drake)


def avr_calc(v_dict):
    empty_list = [0, 0, 0]
    for key in v_dict.keys():
        empty_list[0] += v_dict[key][0]
        empty_list[1] += v_dict[key][1]
        empty_list[2] += v_dict[key][2]
    for i in range(len(empty_list)):
        empty_list[i] /= len(v_dict.keys())
    return empty_list


num = int(input())
drakes = {}

for _ in range(num):
    data = input()
    d_type, name, dmg, hp, ar = null_checker(data)

    if d_type not in drakes:
        drakes[d_type] = {}
    if name in drakes[d_type]:
        drakes[d_type][name] = []
    drakes[d_type][name] = [dmg, hp, ar]

for k, v in drakes.items():
    avr_stats = avr_calc(v)
    print(f"{k}::({avr_stats[0]:.2f}/{avr_stats[1]:.2f}/{avr_stats[2]:.2f})")
    for d_name in sorted(v.items(), key=lambda kvp: kvp[0]):
        print(f"-{d_name[0]} -> damage: {d_name[1][0]}, health: {d_name[1][1]}, armor: {d_name[1][2]}")
