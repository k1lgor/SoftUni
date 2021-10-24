rest_days = int(input())

left_days = 365 - rest_days
time_for_play = left_days * 63 + rest_days * 127
diff = abs(30000 - time_for_play)

h = diff // 60
m = diff % 60

if time_for_play > 30000:
    print(f'Tom will run away\n{h} hours and {m} minutes more for play')
else:
    print(f'Tom sleeps well\n{h} hours and {m} minutes less for play')
