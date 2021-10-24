period = int(input())
treated = 0
untreated = 0
doctors = 7
for i in range(1, period + 1):
    patient = int(input())
    if i % 3 == 0 and untreated > treated:
        doctors += 1
    if doctors >= patient:
        treated += patient
    else:
        untreated += patient - doctors
        treated += doctors
print(f'Treated patients: {treated}.\nUntreated patients: {untreated}.')
