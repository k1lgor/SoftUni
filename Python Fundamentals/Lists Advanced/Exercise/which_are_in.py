substring = input().split(', ')
string = input().split(', ')

substring_list = []

for i in substring:
    for j in string:


        if (pos := j.find(i, 0)) != -1:
            substring_list.append(i)
            break
print(substring_list)
