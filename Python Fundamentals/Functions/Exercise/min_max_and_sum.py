def MIN():
    min_value = min(nums)
    print(f'The minimum number is {min_value}')
def MAX():
    max_value = max(nums)
    print(f'The maximum number is {max_value}')
def SUM():
    sum_value = sum(nums)
    print(f'The sum number is: {sum_value}')
    
nums = [int(num) for num in input().split()]
MIN()
MAX()
SUM()