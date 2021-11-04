command = input()
DICT = {}

while not command.isdigit():
    name, number = command.split('-')
    DICT[name] = number
    command = input()

for _ in range(int(command)):
    search_name = input()
    if search_name in DICT:
        print(f"{search_name} -> {DICT[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
