days, daily, expected = int(input()), int(input()), float(input())
total_plunder = 0
gained_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily
    if day % 3 == 0:
        total_plunder += daily / 2
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(
        f"Collected only {total_plunder * 100 / expected:.2f}% of the plunder.")
