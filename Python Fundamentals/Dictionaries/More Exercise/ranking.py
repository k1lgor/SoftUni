command = input()
all_contests = {}

while command != "end of contests":
    lang, password = command.split(":")
    all_contests.update({lang: password})
    command = input()

all_submissions = {}
command = input()

is_item = False
while command != "end of submissions":
    lang, password, username, points = command.split("=>")
    points = int(points)
    if lang in all_contests and all_contests[lang] == password:
        if username in all_submissions:
            is_item = False
            for i in all_submissions[username]:
                if lang == i['name']:
                    is_item = True
                    i["points"] = max(i["points"], points)
            if not is_item:
                all_submissions[username].append({"name": lang, "points": points})
        else:
            all_submissions[username] = [{"name": lang, "points": points}]
    command = input()

best_points = {}
for student, courses in sorted(all_submissions.items(), key=lambda x: x[0], reverse=False):
    sorted_courses = sorted(courses, key=lambda c: -c['points'])
    total_points = sum(course['points'] for course in courses)
    best_points[student] = total_points

best_student = sorted(best_points.items(), key=lambda p: -p[1])

name, best_points = best_student[0]
print(f"Best candidate is {name} with total {best_points} points.")
print("Ranking:")

for student, courses in sorted(all_submissions.items(), key=lambda x: x[0], reverse=False):
    print(student)
    for course in sorted(courses, key=lambda z: -z['points']):
        print(f"#  {course['name']} -> {course['points']}")
