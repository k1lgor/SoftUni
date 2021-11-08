def passwd_checker(curr_validity, curr_lang, curr_passwd):
    curr_validity[curr_lang] = curr_passwd
    return curr_validity


def users(curr_results, curr_lang, curr_passwd, curr_username, curr_points, curr_validity):
    if curr_lang in curr_validity and curr_passwd == curr_validity[curr_lang]:
        if curr_username not in curr_results:
            curr_results[curr_username] = {curr_lang: curr_points}
        elif curr_lang not in curr_results[curr_username]:
            curr_results[curr_username][curr_lang] = curr_points
        else:
            curr_results[curr_username][curr_lang] = max(curr_results[curr_username][curr_lang], curr_points)
    return curr_results


data = input()
validity = {}

while data != 'end of contests':
    lang, passwd = data.split(":")
    validity = passwd_checker(validity, lang, passwd)
    data = input()

data = input()
results = {}

while data != 'end of submissions':
    lang, passwd, username, points = data.split("=>")
    points = int(points)
    results = users(results, lang, passwd, username, points, validity)

    data = input()

best_result = {}
for k, v in results.items():
    best_result[k] = 0
    for x, z in v.items():
        best_result[k] += z
max_ = max(best_result.items(), key=lambda kvp: kvp[1])
print(f"Best candidate is {max_[0]} with total {max_[1]} points.\nRanking:")
for k, v in sorted(results.items(), key=lambda kvp: kvp[0]):
    print(k)
    for x, z in sorted(v.items(), key=lambda kvp: -kvp[1]):
        print(f"#  {x} -> {z}")
