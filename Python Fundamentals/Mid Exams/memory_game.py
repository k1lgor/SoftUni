elements = input().split()

end = False
for moves in range(1, len(elements) + 1):

    command = input()

    if elements == []:
        end = True
        break

    if command == 'end':
        break

    add = f'-{moves}a'
    index_1, index_2 = command.split()

    if index_1 == index_2 or (int(index_1) < 0 or int(index_2) < 0) or int(index_1) >= len(elements) or int(index_2) >= len(elements):
        length = len(elements) // 2
        elements.insert(length, add)
        elements.insert(length, add)
        print("Invalid input! Adding additional elements to the board")
        continue
    if elements[int(index_1)] == elements[int(index_2)]:
        print(
            f"Congrats! You have found matching elements - {elements[int(index_1)]}!")
        elements.remove(elements[int(index_1)])
        if int(index_2) == 0:
            elements.remove(elements[int(index_2)])
        else:
            elements.remove(elements[int(index_2) - 1])
    else:
        print("Try again!")


if end:
    print(f"You have won in {moves - 1} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
