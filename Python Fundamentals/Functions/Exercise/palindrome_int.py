def check():
    for element in nums:
        if element == element[::-1]:
            print('True')
        else:
            print('False')
            
nums = input().split(', ')
check()