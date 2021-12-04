import re


def raid(n):
    for _ in range(n):
        boss = input()
        match = re.match(r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#", boss)
        if match:
            print(f"{match.group(1)}, The {match.group(2)}\n>> Strength: {len(match.group(1))}\n>> Armour: {len(match.group(2))}")
        else:
            print("Access denied!")


number = int(input())
raid(number)
