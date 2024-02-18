def add(m, tok0):
    if tok0 in m:
        print(f"{tok0} is already registered")
    else:
        m[tok0] = []
    return m


def send(m, tok0, tok1):
    m[tok0].append(tok1)
    return m


def delete(m, tok0):
    if tok0 in m:
        del m[tok0]
    else:
        print(f"{tok0} not found!")
    return m


data = input()
msg = {}
while "Statistics" not in data:
    command, *tokens = data.split("->")
    if command == "Add":
        add(msg, tokens[0])
    elif command == "Send":
        send(msg, tokens[0], tokens[1])
    elif command == "Delete":
        delete(msg, tokens[0])
    data = input()

print(f"Users count: {len(msg)}")
for k, v in sorted(msg.items(), key=lambda x: (-len(x[1]), x[0])):
    print(k)
    for vv in v:
        print(f" - {vv}")
