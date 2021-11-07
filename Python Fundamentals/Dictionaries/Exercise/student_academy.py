num = int(input())
info = {}
for _ in range(num):
    name, grade = input(), float(input())
    if name not in info:
        info[name] = []
    info[name].append(grade)

average = {
    student: sum(info[student]) / len(info[student]) for student in info
}
info.clear()
for k, v in average.items():
    if v >= 4.5:
        info[k] = v
for student in sorted(info, key=info.get, reverse=True):
    print(f"{student} -> {info[student]:.2f}")
