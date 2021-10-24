dest = input()

while dest != 'End':
    budget = float(input())
    ttl = 0

    while ttl < budget:
        ttl += float(input())
    print(f'Going to {dest}!')
    dest = input()
