DICT = {}

while True:
    student = input()

    if ":" not in student:
        end_command = student
        break

    name, ID, course = student.split(":")
    if course not in DICT:
        DICT[course] = {}
    DICT[course][ID] = name

end_command = end_command.replace("_", " ")
current_course = DICT[end_command]

for k, v in current_course.items():
    print(f"{v} - {k}")
