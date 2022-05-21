import re


def raid(n):
    for _ in range(n):
        boss = input()
        if match := re.match(r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#", boss):
            print(
                f"{match[1]}, The {match[2]}\n>> Strength: {len(match[1])}\n>> Armour: {len(match[2])}")

        else:
            print("Access denied!")


number = int(input())
raid(number)
