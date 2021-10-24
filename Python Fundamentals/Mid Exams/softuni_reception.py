emp1, emp2, emp3 = int(input()), int(input()), int(input())
students = int(input())
hours = 0

per_hour = emp1 + emp2 + emp3

while students != 0:

    if per_hour <= students:
        hours += 1
        students -= per_hour
    elif per_hour >= students:
        hours += 1
        students -= students
    if hours % 4 == 0:
        students += per_hour

print(f"Time needed: {hours}h.")
