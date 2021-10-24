jury = int(input())
presentation = ''
grade_counter = 0
ttl_grade = 0.0
while presentation != 'Finish':
    presentation = input()
    if presentation == 'Finish':
        break
    grade = 0.0
    counter = 0
    while True:
        grade += float(input())
        counter += 1
        if counter == jury:
            print(f'{presentation} - {(grade / jury):.2f}.')
            break
    ttl_grade += grade
    grade_counter += counter
print(f'Student\'s final assessment is {(ttl_grade / grade_counter):.2f}.')
