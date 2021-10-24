n = input().split()
k = int(input())
start = 0
exe = []
for _ in range(len(n)):
    start = (start + k - 1) % len(n)
    exe.append(n.pop(start))
result = '[' + ','.join(exe) + ']'
print(result, end='')
