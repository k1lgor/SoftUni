import math
income = float(input())
avr_grade = float(input())
min_work_sal = float(input())
soc_scholar = 0.0
exc_scholar = 0.0

if income <= min_work_sal and avr_grade >= 4.5:
    soc_scholar = math.floor(min_work_sal * 0.35)
if avr_grade >= 5.5:
    exc_scholar = math.floor(avr_grade * 25)
if soc_scholar < exc_scholar:
    print(
        f'You get a scholarship for excellent results {exc_scholar} BGN')
elif exc_scholar < soc_scholar:
    print(f'You get a Social scholarship {soc_scholar} BGN')
else:
    print('You cannot get a scholarship!')
