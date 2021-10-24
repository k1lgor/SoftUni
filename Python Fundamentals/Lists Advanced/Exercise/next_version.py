version = [d for i, d in enumerate(str(int(''.join(input().split('.'))) + 1))]
print(f'{version[0]}.{version[1]}.{version[2]}')
