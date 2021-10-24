new_list = list(map(int, input().split()))
count = int(input())

for _ in range(count):
    new_list.remove(min(new_list))
print(', '.join(map(str, new_list)))
