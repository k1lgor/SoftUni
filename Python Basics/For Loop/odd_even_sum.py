even = 0
odd = 0
nl = '\n'
for i in range(1, int(input()) + 1):
    nn = int(input())
    if i % 2 == 0:
        even += nn
    else:
        odd += nn
if even == odd:
    print(f'Yes{nl}Sum = {even}')
else:
    print(f'No{nl}Diff = {abs(even - odd)}')
