nums = list(map(lambda x: int(x), input().split('@')))

curr_index = 0


def mission():

    counter = nums.count(0)
    if counter == len(nums):
        print('Mission was successful.')
    else:
        print(f'Cupid has failed {len(nums) - counter} places.')


while True:

    command = input().split()

    if 'Love!' in command:
        break

    index = int(command[1])
    curr_index += index

    if curr_index >= len(nums):
        curr_index = 0

    if nums[curr_index] != 0:
        nums[curr_index] -= 2
        if nums[curr_index] == 0:
            print(f"Place {curr_index} has Valentine's day.")
    else:
        print(f"Place {curr_index} already had Valentine's day.")

print(f"Cupid's last position was {curr_index}.")

mission()
