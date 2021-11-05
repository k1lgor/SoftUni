command = input()
user = {}

while 'End' not in command:
    company, ID = command.split(" -> ")

    if company not in user:
        user[company] = []
    if ID not in user[company] and company in user:
        user[company].append(ID)

    command = input()

for k, v in sorted(user.items(), key=lambda kvp: kvp[0], reverse=False):
    print(f"{k}")
    single_ID = iter(v)
    for x in single_ID:
        print(f"-- {x}")
