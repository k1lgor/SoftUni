from math import floor

HP = int(input())
virus = input()
virus_catalogue = {}

while "end" not in virus:

    if virus not in virus_catalogue:
        virus_catalogue[virus] = floor(sum(ord(x) for x in virus) / 3)
        defeat = virus_catalogue[virus] * len(virus)
    else:
        defeat = floor(virus_catalogue[virus] * len(virus) / 3)
    m = floor(defeat / 60)
    s = round((defeat / 60) % 1 * 60)

    if HP > virus_catalogue[virus]:
        remaining = floor(HP - defeat)
        print(f"Virus {virus}: {virus_catalogue[virus]} => {defeat} seconds")

    if remaining > 0:
        print(f"{virus} defeated in {m}m {s}s.")
        print(f"Remaining health: {remaining}")
    else:
        print("Immune System Defeated.")
        exit()

    remaining += floor(remaining * 0.2)
    HP = min(remaining, HP)
    virus = input()

print(f"Final Health: {floor(HP)}")
