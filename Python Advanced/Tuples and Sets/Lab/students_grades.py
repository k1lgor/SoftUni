num = int(input())
grades = {}

for _ in range(num):
    name, grade = input().split()
    if name not in grades:
        grades[name] = [format(float(grade), '.2f')]
    else:
        grades[name].append(format(float(grade), '.2f'))

for k, v in grades.items():
    print(f'{k} -> {" ".join(v)} (avg: {sum(float(x) for x in v) / len(v):.2f})')
