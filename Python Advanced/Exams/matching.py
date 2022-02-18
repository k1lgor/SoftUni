from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    if males and not males[-1] % 25 and males[-1] != 0:
        males.pop()
        males.pop()
        continue
    if females and not females[0] % 25 and females[0] != 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
        continue
    if males[-1] != females[0]:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")
if males:
    males.reverse()
    print(f"Males left: {', '.join(str(x) for x in males)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
