def even_odd():
    even = sum(int(num) for num in nums if int(num) % 2 == 0)
    odd = sum(int(num) for num in nums if int(num) % 2 != 0)
    
    print(f'Odd sum = {odd}, Even sum = {even}')
    return even, odd

nums = input()
even, odd = 0, 0
even_odd()