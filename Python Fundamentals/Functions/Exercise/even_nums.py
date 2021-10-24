nums = [int(num) for num in input().split()]
List = []

def even_filter(x):
    return x % 2 == 0
    
even = filter(even_filter, nums)

for x in even:
    List.append(x)
    
print(List)