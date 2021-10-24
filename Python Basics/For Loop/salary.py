tabs = int(input())
salary = int(input())
for _ in range(1, tabs + 1):
    site = str(input())
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(f'{salary}')
