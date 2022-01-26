num = int(input())

guests = {input() for _ in range(num)}

command = input()

while "END" not in command:
    if command in guests:
        guests.discard(command)
    command = input()

print(len(guests))
for res_num in sorted(guests, key=str, reverse=False):
    print(res_num)
