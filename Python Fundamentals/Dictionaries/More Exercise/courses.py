command = input()
courses = {}

while 'end' not in command:
    name, user = command.split(" : ")
    if name not in courses:
        courses[name] = []
    courses[name].append(user)

    command = input()

for k, v in sorted(courses.items(), key=lambda kvp: len(kvp[1]), reverse=True):
    print(f"{k}: {len(v)}")
    for n in sorted(v):
        print(f"-- {n}")
