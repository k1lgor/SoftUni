from math import floor

bis_day_worker, workers, enemy_factory = int(input()), int(input()), int(input())
bis_month = 0
for day in range(1, 31):
    if day % 3 == 0:
        bis_month += (bis_day_worker * workers) * 0.75
        continue
    bis_month += bis_day_worker * workers
print(f"You have produce {floor(bis_month)} biscuits for the past month.")
diff = abs(floor(bis_month) - enemy_factory)
if bis_month > enemy_factory:
    print(f"You produce {diff / enemy_factory * 100:.2f} percent more biscuits.")
if bis_month < enemy_factory:
    print(f"You produce {diff / enemy_factory * 100:.2f} percent less biscuits.")
