nums = list(map(lambda x: int(x), input().split('@')))
curr_index = 0


def love(curr_index):

    if nums[curr_index] == 0:
        return print(f"Place {curr_index} already had Valentine's day.")

    nums[curr_index] -= 2
    if nums[curr_index] == 0:
        return print(f"Place {curr_index} has Valentine's day.")


def mission():

    if (counter := nums.count(0)) == len(nums):
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
    love(curr_index)


print(f"Cupid's last position was {curr_index}.")
mission()
