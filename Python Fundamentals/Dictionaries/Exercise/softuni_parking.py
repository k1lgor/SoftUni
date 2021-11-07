num = int(input())
reg_users = {}

for _ in range(num):
    command, *arg = input().split()

    if command == 'register':
        if arg[0] not in reg_users:
            reg_users[arg[0]] = arg[1]
            print(f"{arg[0]} registered {arg[1]} successfully")
        else:
            print(f"ERROR: already registered with plate number {arg[1]}")

    if command == 'unregister':
        if arg[0] not in reg_users:
            print(f"ERROR: user {arg[0]} not found")
        else:
            print(f"{arg[0]} unregistered successfully")
            reg_users.pop(arg[0])

for k, v in reg_users.items():
    print(f"{k} => {v}")
