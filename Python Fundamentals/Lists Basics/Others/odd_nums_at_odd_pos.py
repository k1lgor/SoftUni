l = input().split()

for i, d in enumerate(l):
    odd_num = 0
    odd_index = 0
    if i % 2 != 0 and int(d) % 2 != 0:
        odd_num, odd_index = int(d), i 
        print(f'Index {odd_index} -> {odd_num}')
    else:
        None

