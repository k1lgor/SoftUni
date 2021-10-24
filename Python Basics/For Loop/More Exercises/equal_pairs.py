n = int(input())
left = 0
middle = 0
diff = 0
maxdiff = 0
for i in range(n):
    middle = left
    left = 0
    left += int(input())
    left += int(input())
    if i != 0:
        diff = abs(left - middle)
        if diff != 0 and diff > maxdiff:
            maxdiff = diff
if middle == left or n == 1:
    print(f'Yes, value={left}')
else:
    print(f'No, maxdiff={maxdiff}')
