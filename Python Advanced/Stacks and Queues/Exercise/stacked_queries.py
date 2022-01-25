num = int(input())
queue = []

for _ in range(num):
    command = input().split(' ')
    if command[0] == '1':
        queue.append(int(command[1]))
    elif command[0] == '2' and queue:
        queue.pop()
    elif command[0] == '3' and queue:
        print(max(queue))
    elif command[0] == '4' and queue:
        print(min(queue))

mun = []
while queue:
    mun.append(queue.pop())
print(*mun, sep=', ')
