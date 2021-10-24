students, lectures, bonus = int(input()), int(input()), int(input())
total_bonus = 0
max_attendace = 0
max_bonus = 0

for student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)

    if attendance > max_attendace:
        max_attendace = attendance
        max_bonus = total_bonus

print(
    f"Max Bonus: {round(max_bonus)}.\nThe student has attended {max_attendace} lectures.")
