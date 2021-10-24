n = int(input())

print(f"+{' -' * (n - 2)} +")

for _ in range(n - 2):
    print(f"|{' -' * (n - 2)} |")

print(f"+{' -' * (n - 2)} +")
