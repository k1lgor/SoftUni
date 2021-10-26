fr = input().split(", ")
blacklisted_count = 0
lost_count = 0

while True:

    command, *args = input().split()

    if command == 'Report':
        break

    if command == 'Blacklist':
        if args[0] in fr:
            index = fr.index(args[0])
            print(f"{args[0]} was blacklisted.")
            fr[index] = 'Blacklisted'
            blacklisted_count += 1
        else:
            print(f"{args[0]} was not found.")
    if (
        command == 'Error'
        and 0 <= int(args[0]) < len(fr)
        and fr[int(args[0])] not in ['Blacklisted', 'Lost']
    ):
        print(f"{fr[int(args[0])]} was lost due to an error.")
        fr[int(args[0])] = 'Lost'
        lost_count += 1
    if command == 'Change' and 0 <= int(args[0]) < len(fr):
        print(f"{fr[int(args[0])]} changed his username to {args[1]}.")
        fr[int(args[0])] = args[1]

print(
    f"Blacklisted names: {blacklisted_count}\nLost names: {lost_count}\n{' '.join(fr)}")
