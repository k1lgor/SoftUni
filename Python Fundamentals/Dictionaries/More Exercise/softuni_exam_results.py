def store(temp_result, temp_name, temp_points):
    if (
            temp_name in temp_result
            and temp_result[temp_name] < temp_points
            or temp_name not in temp_result
    ):
        temp_result[temp_name] = temp_points
    return temp_result


def storage(temp_submissions, temp_language, temp_points):
    if temp_language not in temp_submissions:
        temp_submissions[temp_language] = []
    temp_submissions[temp_language].append(temp_points)
    return temp_submissions


command = input()
result = {}
submissions = {}
while command != "exam finished":
    name, *arg = command.split("-")
    if arg[0] != 'banned':
        language = arg[0]
        points = int(arg[1])
        result = store(result, name, points)
        submissions = storage(submissions, language, points)
    else:
        del result[name]
    command = input()

print("Results:")
for k, v in sorted(result.items(), key=lambda kvpt: (-kvpt[1], kvpt[0])):
    print(f"{k} | {v}")
print("Submissions:")
for k, v in sorted(submissions.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0])):
    print(f"{k} - {len(v)}")
