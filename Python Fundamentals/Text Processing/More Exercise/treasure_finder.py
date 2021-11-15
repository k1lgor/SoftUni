keys = list(map(lambda x: int(x), input().split()))
command = [x for x in input()]

while 'find' not in command:
    counter = 0
    hidden_msg = ''
    hidden_word = ''
    hidden_coord = ''

    for char in command:
        if counter == len(keys):
            counter = 0
        hidden_msg += chr(ord(char) - keys[counter])
        counter += 1

    index_item = hidden_msg.index("&")

    for x in hidden_msg[index_item + 1:]:
        if x != "&":
            hidden_word += x
        else:
            break

    index_coord1 = hidden_msg.index("<")
    index_coord2 = hidden_msg.index(">")
    hidden_coord = hidden_msg[index_coord1 + 1:index_coord2]

    print(f"Found {hidden_word} at {hidden_coord}")

    command = input()
