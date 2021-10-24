budget = float(input())
actor = ''
salary = 0
while actor != 'ACTION':
    actor = input()
    if actor == 'ACTION':
        print(f'We are left with {budget:.2f} leva.')
        break
    name_len = len(actor)
    if name_len > 15:
        budget *= 0.8
        continue
    salary = float(input())
    budget -= salary
    actor = ''
    salary = 0
    if budget < 0:
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break

