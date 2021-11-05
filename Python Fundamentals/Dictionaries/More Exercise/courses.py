command = input()
courses = {}

while 'end' not in command:
    name, user = command.split(" : ")
    if name not in courses:
        courses[name] = []
    courses[name].append(user)

    command = input()

sort_by_number = sorted(courses.items(), key=lambda kvp: len(kvp[1]), reverse=True)
for k, v in sort_by_number:
    print(f"{k}: {len(v)}")
    sort_by_name = sorted(v, key=str)
    for n in sort_by_name:
        print(f"-- {n}")
