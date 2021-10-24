days = int(input())
hrs_per_day = int(input())
tax = 0
cur_tax = 0
for i in range(1, days + 1):
    for j in range(1, hrs_per_day + 1):
        if i % 2 == 0 and j % 2 != 0:
            cur_tax += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            cur_tax += 1.25
        else:
            cur_tax += 1
    print(f'Day: {i} - {cur_tax:.2f} leva')
    tax += cur_tax
    cur_tax = 0
print(f'Total: {tax:.2f} leva')
