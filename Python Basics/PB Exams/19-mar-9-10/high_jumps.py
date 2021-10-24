wanted_height = int(input())
cur_height = wanted_height - 30
counter = 0
fail_counter = 0

while cur_height <= wanted_height:
    height = int(input())

    if height > cur_height:
        cur_height += 5
        fail_counter = 0
    else:
        fail_counter += 1
    counter += 1
    if fail_counter == 3:
        break

if fail_counter == 3:
    print(f'Tihomir failed at {cur_height}cm after {counter} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {wanted_height}cm after {counter} jumps.')