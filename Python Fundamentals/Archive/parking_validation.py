def validation(d, r, v):
    def license_plate(tok1, vv):
        if len(tok1) != 8:
            return
        first_last = tok1[:2] + tok1[-2:]
        middle = tok1[2:6]
        for i in first_last:
            if i.isupper():
                continue
            vv = True
            return vv
        for i in middle:
            if i.isdigit():
                continue
            vv = True
            return vv

    def user(tok0, tok1, rr):
        if tok1 in rr.values():
            print(f"ERROR: license plate {tok1} is busy")
        elif tok0 not in rr:
            rr[tok0] = tok1
            print(f"{tok0} registered {tok1} successfully")
        else:
            print(f"ERROR: already registered with plate number {rr[tok0]}")

        return rr

    def checker(tok0, rr):
        if tok0 not in rr:
            print(f"ERROR: user {tok0} not found")
        else:
            print(f"user {tok0} unregistered successfully")
            del rr[tok0]
        return rr

    command, *tokens = d.split()
    if command == "register":
        if license_plate(tokens[1], v):
            print(f"ERROR: invalid license plate {tokens[1]}")
            return False
        elif user(tokens[0], tokens[1], r):
            return True
    elif command == "unregister":
        checker(tokens[0], r)
        return True


number = int(input())
register = {}
valid = False

for _ in range(number):
    data = input()
    validation(data, register, valid)

for k, v in register.items():
    print(f"{k} => {v}")
