content = input()
students = {}
judge = {}
new_students = {}
is_item = False
while content != "no more time":
    username, course, points = content.split(" -> ")
    points = int(points)
    if course in judge:
        is_username_participated = False
        for item in judge[course]:

            if username == item['name']:
                is_username_participated = True
                item["points"] = max(item["points"], points)
        if not is_username_participated:
            judge[course].append({"name": username, "points": points})

    else:
        judge[course] = [{"name": username, "points": points}]
    if username in students:
        students[username] += points
    else:
        students[username] = points
    content = input()

for course, value_ in judge.items():
    print(f'{course}: {len(value_)} participants')

    sorted_st = sorted(judge[course], key=lambda p: (-p['points'], p['name']))
    for index in range(len(sorted_st)):
        name, points = sorted_st[index].values()
        print(f"{index + 1}. {name} <::> {points}")

print("Individual standings:")

all_points = 0
for course, value in judge.items():
    for user in value:
        name = user['name']
        points = user['points']
        if name in new_students:
            new_students[name] += points
        else:
            new_students[name] = points

sorted_students = sorted(new_students.items(), key=lambda x: (-x[1], x[0]))
for i in range(len(sorted_students)):
    name, points = sorted_students[i]
    print(f"{i + 1}. {name} -> {points}")
