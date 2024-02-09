nums = list(map(int, input().split()))

while True:
    
    if (command := input()) == 'Finish':
        print(*nums, sep=' ')
        break
    
    action, *args = command.split()
    
    if action == 'Add':
        nums.append(int(args[0]))
    if action == 'Remove':
        for index in range(len(nums)):
            if nums[index] == int(args[0]):
                nums.pop(index)
                break
    if action == 'Replace':
        for index in range(len(nums)):
            if nums[index] == int(args[0]):
                nums.insert(index, int(args[1]))
                nums.pop(index + 1)
                break
    if action == 'Collapse':
        nums = [x for x in nums if int(args[0]) <= x]
