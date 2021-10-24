exam_hr = int(input())
exam_min = int(input())
arr_hr = int(input())
arr_min = int(input())

exam_in_min = exam_hr * 60 + exam_min
arr_in_min = arr_hr * 60 + arr_min
diff = abs(arr_in_min - exam_in_min)

if arr_in_min > exam_in_min:
    print('Late')
elif diff <= 30:
    print('On time')
else:
    print('Early')

if exam_in_min - arr_in_min > 0:
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        print(f'{diff // 60}:{diff % 60:02d} hours before the start')
elif arr_in_min - exam_in_min > 0:
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{diff // 60}:{diff % 60:02d} hours after the start')
