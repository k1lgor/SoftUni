energy, distance = int(input()), input()
won_battle = 0

while True:

    if won_battle % 3 == 0:
        energy += won_battle

    if 'End of battle' in distance:
        print(f"Won battles: {won_battle}. Energy left: {energy}")
        break

    if energy < int(distance):
        energy = max(energy, 0)
        print(
            f"Not enough energy! Game ends with {won_battle} won battles and {energy} energy")
        break

    energy -= int(distance)
    won_battle += 1

    distance = input()
